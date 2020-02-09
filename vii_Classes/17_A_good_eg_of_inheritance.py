class InvalidOperationError(Exception):
    # derived from base exception class in python
    # always call the class whenever building a custom one
    pass


class Stream:
    # a base class
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            # we create a custom exception as python doesn't have one
            raise InvalidOperationError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


movie = Stream()

