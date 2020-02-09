class IphoneType:
    def __init__(self):
        self.iphone = {}

    def __setitem__(self, key, value):
        self.iphone[key] = value

    def __getitem__(self, item):
        return self.iphone[item]


Iphone = IphoneType()
Iphone["4"] = "2010"
print(Iphone["4"])
