class Human():
    def __init__(self, name, friends):
        self.name = name
        self.friends = friends

    def AddFriends(self,addFriend):
        self.friends.append(addFriend)

    def GetName(self):
        print(self.name)

    def GetFriends(self):
        print(self.friends)

human = Human('유종훈',['김철수','김영희'])
human.AddFriends('김범수')
human.GetName()
human.GetFriends()