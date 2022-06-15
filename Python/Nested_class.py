class Army:
    def __init__(self):
        self.battalion_name = "Gorkha"
        self.gn = self.Gun()  # Creating inner Class Object

    def disp(self):
        print("Battalion Name:", self.battalion_name)

    class Gun:  # Nested class
        def __init__(self):
            self.ak_47 = "AK 47 English Gun"
            self.rifle = "Old war rifles 1947"
            self.snip = "Snipper Rifle"

        def disp(self):
            print("Fast Gun:", self.ak_47)
            print("Old class rifle: ", self.rifle)
            print("Long range gun: ", self.snip)


obj = Army()
print(obj.gn.ak_47)  # Outer class object -> Inner class object --> variable name
print(obj.gn.snip)  # Outer class object -> Inner class object --> variable name
print()
obj.gn.disp()
