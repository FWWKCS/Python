friendList = []
class Human:
    def __init__(self):
        pass

    def AddFriend(self, FriendName):
        self.FriendName = FriendName
        friendList.append(FriendName)
        
    def GetFriends(self):
        print(friendList)

human = Human()
human.AddFriend('김하나')
human.AddFriend('김기리')
human.GetFriends()