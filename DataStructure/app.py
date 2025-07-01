from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'library_secret'

def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.template_global()
def now():
    return datetime.now().strftime('%Y-%m-%d')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        conn = get_db_connection()
        student = conn.execute('SELECT * FROM students WHERE name = ? AND password = ?', 
                               (name, password)).fetchone()
        conn.close()
        if student:
            session['student_id'] = student['id']
            session['name'] = student['name']
            return redirect('/dashboard')
        else:
            error = 'Invalid credentials.'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'student_id' not in session:
        return redirect('/')
    conn = get_db_connection()
    borrowed = conn.execute('''
        SELECT b.title, br.due_date, br.returned 
        FROM borrowed br JOIN books b ON br.book_id = b.id 
        WHERE br.student_id = ?
    ''', (session['student_id'],)).fetchall()
    conn.close()
    return render_template('dashboard.html', borrowed=borrowed, name=session['name'])

@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    if 'student_id' not in session:
        return redirect('/')
    conn = get_db_connection()
    if request.method == 'POST':
        book_id = request.form['book_id']
        due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
        conn.execute('INSERT INTO borrowed (student_id, book_id, due_date, returned) VALUES (?, ?, ?, 0)', 
                     (session['student_id'], book_id, due_date))
        conn.execute('UPDATE books SET available = available - 1 WHERE id = ?', (book_id,))
        conn.commit()
        return redirect('/dashboard')
    books = conn.execute('SELECT * FROM books WHERE available > 0').fetchall()
    conn.close()
    return render_template('borrow.html', books=books)

@app.route('/return', methods=['GET', 'POST'])
def return_book():
    if 'student_id' not in session:
        return redirect('/')
    conn = get_db_connection()
    if request.method == 'POST':
        borrowed_id = request.form['borrowed_id']
        book_id = conn.execute('SELECT book_id FROM borrowed WHERE id = ?', 
                               (borrowed_id,)).fetchone()['book_id']
        conn.execute('UPDATE borrowed SET returned = 1 WHERE id = ?', (borrowed_id,))
        conn.execute('UPDATE books SET available = available + 1 WHERE id = ?', (book_id,))
        conn.commit()
        return redirect('/dashboard')
    borrowed = conn.execute('''
        SELECT br.id, b.title 
        FROM borrowed br JOIN books b ON br.book_id = b.id 
        WHERE br.student_id = ? AND br.returned = 0
    ''', (session['student_id'],)).fetchall()
    conn.close()
    return render_template('return.html', borrowed=borrowed)
    
if __name__ == '__main__':
    app.run(debug=True)
