class Duck:
    def walk(self):
        print("thapak thapak thapak tahapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)