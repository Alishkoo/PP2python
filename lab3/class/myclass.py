class Myclass:
    def __init__(self, color, size):
        self.color = color
        self.size = size


    def __del__(self):
        print("Deleted the object")


    def get_color(self):
        print(self.color)


    def set_color(self, color):
        self.color = color


a = Myclass('red', 2)
a.set_color("green")
a.get_color()