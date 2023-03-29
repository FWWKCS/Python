class Human():
    def __init__(self, name, friends):
        self.name = name
        self.friends = friends

    def GetFriends(self, count):
        for i in range(count):
            print(self.friends[i])

human = Human('유종훈',['김철수','김영희','박영수','이미자'])
human.GetFriends(3)
human.GetFriends(1)