class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.lower())
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)  # calling a method of the super/base class


list = TrackableList()
list.append("1")
