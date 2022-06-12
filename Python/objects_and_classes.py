class PostalAddress:
    zip = 12345

    def __init__(self, name="default", street="default"):
        self.name = name
        self.street = street
        # self.zip = PostalAddress.zip

    def changeName(self, newName):
        self.name = newName

    @classmethod
    def changeZip(cls, newZip):
        cls.zip = newZip


p1 = PostalAddress("ABC", "Rohini")
p2 = PostalAddress("DEF", "Dwarka")
PostalAddress.changeZip(234567)

print(p1.__dict__)
print(p2.__dict__)
print(PostalAddress.__dict__)
