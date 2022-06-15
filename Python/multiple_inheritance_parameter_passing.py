class First():
    def __init__(self, first, **kwargs):
        print("Class First")
        super(First, self).__init__(**kwargs)
        self.first = first
        print("First:", self.first)


class Second():
    def __init__(self, second, **kwargs):
        print("Class Second")
        super(Second, self).__init__(**kwargs)
        self.second = second
        print("Second:", self.second)


class Third():
    def __init__(self, third, **kwargs):
        print("Class Third")
        super(Third, self).__init__(**kwargs)
        self.third = third
        print(self.third)


class Combined(First, Second):
    def __init__(self, first, second):
        super(Combined, self).__init__(first=first, second=second)


obj = Combined("First", "Second")
