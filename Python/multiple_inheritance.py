class State():
    def __init__(self):
        print("INIT of State!")
        self.state_first = "State Base"


class Event():
    def __init__(self):
        self.event_name = "Event State"
        print("INIT of Event")


#
# class HappyState(State, Event):
# 
#     def __init__(self):
#         print("INIT of Happy State")
#         self.state_second = "Happy State (Child)"
#         State.__init__(self)
#         Event.__init__(self)
# or


class HappyState(State, Event):

    def __init__(self):
        print("INIT of Happy State")
        self.state_second = "Happy State (Child)"
        super(HappyState, self).__init__()
        super(State, self).__init__()

# Note: With this way we will introduce dependency injection means
# class HappyState -> State -> Event  they all are dependent to each other for calling

obj = HappyState()
print(obj.__dict__)
