# Duck Typing 'If it walk like a Duck and talks like a duck, it must be a duck'
# which means python doesn't care about which class of object it is, if it is an
# object and required behavior is present for the object then it will work.

class Duck:
    def walk(self):
        print("Walking like a duck")


class Horse:
    def walk(self):
        print("Walking like a horse")


def myfunction(obj):
    obj.walk()


duck_obj = Duck()
horse_obj = Horse()
myfunction(duck_obj)
myfunction(horse_obj)
