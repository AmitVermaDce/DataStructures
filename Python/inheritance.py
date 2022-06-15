class State():
    def __init__(self, state_name):
        print("Init called!!!")
        self.state_name = state_name


class HappyState(State):

    def __init__(self, name):
        super().__init__(name)
        print("Happy State Init func")


class SadState(State):

    def __init__(self, name):
        super().__init__(name)
        print("Sad State Init func")


obj = HappyState("Happy")
obj1 = SadState("Sad")
print(obj.__dict__)
print(obj1.__dict__)
