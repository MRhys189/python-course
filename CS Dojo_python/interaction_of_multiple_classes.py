class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)


class Person:
    def __init__(self, n, p, i, r):
        self.name = n
        self.personality = p
        self.is_sitting = i
        self.robot_owned = r

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

    def robot_owner(self):
        self.robot_owned = True

    def not_robot_owner(self):
        self.robot_owned = False


p1 = Person("Jerry", "aggressive", False, True)
p1.robot_owned = r1
p1.robot_owned.introduce_self()

# p1 owns r2
# p1.robot_owned = r2
# p2.robot_owned = r1

# p1.robot_owned.introduce_self()
