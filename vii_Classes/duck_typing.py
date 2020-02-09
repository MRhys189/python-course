class Duck:
    def quack(self):
        print("Quack,quack")

    def fly(self):
        print("Flap, flap")


class Person:

    def quack(self):
        print("I'm quacking like a duck!")

    def fly(self):
        print("I'm flapping my arms!")


def quack_and_fly(thing):
    # Not duck-typed(Non-pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("This has to be a Duck!")

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
