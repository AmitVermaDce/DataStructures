class Mobile:
    fp = "Yes"  # class variable

    def __init__(self, name):
        self.model = name

    def show_model(self):
        print("Model:", self.model)

    @classmethod
    def is_fingerprint(cls):  # class Method
        return cls.fp  # accessing class variable inside class method


phone1 = Mobile("Xioami")
phone1.show_model()
print("Is figerprint:", phone1.is_fingerprint())
print()
phone2 = Mobile("One Plus 9")
phone2.show_model()
print("Is figerprint:", phone2.is_fingerprint())
