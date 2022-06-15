class Mobile:
    def __init__(self, m, v=80):
        print("I am constructor with parameters")
        self.model = m
        self.version = v

    def disp(self, p):
        self.price = p
        print("Model: ", self.model)
        print("Version: ", self.version)
        print("Price: ", self.price)


# Passing arguments to the constructor
obj = Mobile("RealMe X", 50)

# Accessing methods from outside the class
obj.disp(10000)
