#write a python programme to stimulate the behaviour of a webpage or web browsers back button when a user visits a new page push it to the stack when the user cliic                     ks back pop the top page and go back to the previous page
class Browser:
    def __init__(self):
        self.history=[]
    def visit(self,page):
        self.history.append(page)
        print(f"visited {page}")
    def Undo(self):
        if len(self.history)>1:
            self.history.pop()
            print(f"Back to {self.history[-1]}")
        else:
            print("no pages to comeback")
browser=Browser()
browser=visit('googlre.com')
browser=visit('linkedin.com')
browser=visit ('github.com')
browser.Undo()