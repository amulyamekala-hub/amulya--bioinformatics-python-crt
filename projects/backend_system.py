'''
Desgin a backend system to manage multiplayer game tournaments. 
players register play matches, and earn points. the syatem should
rank them, handle tiebreaker, and stimulate knockout rounds:
---------------
player registration with unique username.
Match results entry and automatic point updates.
Leaderboard sorted by score.
Simulate knockout using recursion.
Export match history.
Tech Stack: 
--------------
Core Python (Lists, Dictionaries, Tuples)
OOP(Player, Match, Tournament classes)
Recursion (knockout simulation)
Sorting Algorithms(Leaderboard)
File Handling (History logs)
Optional: Pandas for final score export
'''
import random
class Player:
    def __init__(self,username):
        self.username=username
        self.score=0
class Match:
    def __init__(self,player1,player2,winner):
        self.player1=player1
        self.player2=player2
        self.winner=winner
class Tournamnet:
    def __init__(self):
        self.players={}
        self.matches=[]
    def register_player(self,username):
        if username in self.players:
            print(f"{username}already registeres.")
        else:
            self.players[username]=Player(username)
            print(f"{username} registered.")
    def add_match_result(self,username1,username2,username3,winner_name):
        if winner_name not in [username1,username2]:
            print("Winner must be one of the two players.")
            return
        if username1 not in self.players or username2 not in self.players:
            print("Players(s) not registered.")
            return
        winner=self.players[winner_name]
        winner.scroe +=3
        match=Match(username1,username2,winner_name)
        winner.score+=3
        match=Match(username1,username2,winner_name)
        self.matches.append(match)
        print(f"{username1} vs {username2}=> {winner_name}")
    def display_leaderboard(self):
        sorted_players=sorted(self.players.values(),key=lambda p:(-p.score,p.username))
        for i,player in enumerate (sorted_players,1):
            print(f"{i}.{player.username}-{player.score}")

