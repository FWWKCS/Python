class Human():
    def __init__(self, *friend):
        self.friend = friend

    def GetFriends(self):
        print(list(self.friend))

human = Human('유종훈','조현호')
human.GetFriends()