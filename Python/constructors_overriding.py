class Father(object):
    def __init__(self, m):
        self.money = m
        print("--Father class constructor--")

    def show(self):
        print("Father class instance method.")


class Son(Father):
    def __init__(self, m, job):
        super(Son, self).__init__(m)
        self.job = job
        print("---Son class constructor---")

    def disp(self):
        print("Son class Instance method\n")
        print("Money: ", self.money)
        print("Job: ", self.job)


obj = Son(800, "Machine Learning Engineer")
obj.disp()
