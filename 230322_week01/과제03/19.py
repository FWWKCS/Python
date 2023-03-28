class Human:
    def __init__(self, name, fList):
        self.name = name
        self.fList = fList

    def AddFriend(self, FriendName):
        self.FriendName = FriendName
        self.fList.append(self.FriendName)
        
    def GetFriends(self):
        print(f"{self.name} 친구목록")
        print(f'- {self.fList[0]}')
        print(f'- {self.fList[1]}')

human = Human('유종훈',['김철수','김영희'])

human.GetFriends()