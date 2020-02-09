# a class that keeps track of various tags in a blog
class TagCloud:
    def __init__(self):
        self.__tags = {} #makes the Tag attribute private and harder to access outside

    def add(self, tag):
        self.__tags[tag] = self.__tags.get(tag.lower, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):  # to make the __len__() iterable
        return iter(self.__tags)


cloud = TagCloud()
print(cloud._TagCloud__tags)
