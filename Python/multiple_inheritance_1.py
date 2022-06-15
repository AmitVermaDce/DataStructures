class First():
    def __init__(self):
        print("Class First")
        super(First, self).__init__()


class Second():
    def __init__(self):
        print("Class Second")
        super(Second, self).__init__()


class Third():
    def __init__(self):
        print("Class Third")
        super(Third, self).__init__()


class Combined(First, Second, Third):
    def __init__(self):
        super(Combined, self).__init__()


obj = Combined()
