from collections import deque
import matplotlib.pyplot as plt
class openMic:
    def __init__(self):
        self.performers=[]
        self.audience=set()
        self.queue=deque()
        self.votes={}
        self.voted={}
    def register(self,name,role):
        if role == "performer" and name not in self.performers:
            self.performers.append(name)
            self.queue.append(name)
            self.votes[name]=0
        elif role=="audience" and name not in self.audience:
            self.audience.add(name)
            self.voted[name]=set()
    def start(self):
        while self.queue:
            p=self.queue.popleft()
            for a in self.audience:
                if p not in self.voted[a]:
                    vote=input(f"{a}, vote for {p}? (y/n):").strip().lower()
                    if vote== "y":
                        self.votes[p]+=1
                        self.voted[a].add(p)
    def winner (self):
        max_v=max(self.votes.values())
        for p in self.votes:
            if self.votes[p]==max_v:
                print(f"winner: {p} with {max_v} votes")
    def save(self,file="result.txt"):
        with open(file,"w")as f:
            for p in self.performers:
                f.write(f"{p} = {self.votes[p]} votes\n")
    def chart(self):
        names,counts=zip(*self.votes.items())
        plt.bar(names,counts)
        plt.title("vote count")
        plt.ylabel("votes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
o=openMic()
o.register("Alice","performer")
o.register("Bob","performer")
o.register("Tom","audience")
o.register("Jerry","audience")
o.start()
o.winner()
o.save()
o.chart()
     
     


