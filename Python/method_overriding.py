class Add:
    def add(self, a, b):
        print("Addition:", a + b)


class Mult(Add):
    def mult(self, a, b):
        super(Mult, self).add(a, b)
        print("Multiplication:", a * b)


obj = Mult()
obj.mult(2, 4)
