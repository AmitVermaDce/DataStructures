class Mobile:
    def __init__(self, m):
        print("I am constructor with parameters")
        self.model = m  # Instance Variable

    def disp(self):  # Instance method
        print(self.model)


obj = Mobile("RealMe X")
print(obj.model)  # Accessing instance variable outside the class
