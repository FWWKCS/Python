class Human:
    def __init__(self, name, fList):
        self.name = name
        self.fList = fList

    def GetName(self):
        print(self.name)

    def AddFriend(self, FriendName):
        self.FriendName = FriendName
        self.fList.append(self.FriendName)
        
    def GetFriends(self):
        print(self.fList)

human = Human('유종훈',['김철수','김영희'])
human.AddFriend('김범수')
human.GetName()
human.GetFriends()