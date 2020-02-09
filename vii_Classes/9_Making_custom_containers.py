# a class that keeps track of various tags in a blog
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag] = self.tags.get(tag.lower, 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self): #to make the __len__() iterable
        return iter(self.tags)


cloud = TagCloud()

cloud["python"]
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
