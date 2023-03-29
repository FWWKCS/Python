class Human():
    def __init__(self, friend0, friend1):
        self.friend0 = friend0
        self.friend1 = friend1

    def GetFirstFriend(self):
        print(self.friend0)
    
    def GetSecondFriend(self):
        print(self.friend1)

human = Human('유종훈','조현호')
human.GetFirstFriend()
human.GetSecondFriend()
    
    
    