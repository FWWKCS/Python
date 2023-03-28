class Human:
    def __init__(self, name, fList):
        self.name = name
        self.fList = fList

    def GetFriends(self, count):
        self.count = count
        for i in range(0,self.count):
            print(self.fList[i])

human = Human('유종훈',['김철수','김영희','박영수','이미자'])

human.GetFriends(3)
human.GetFriends(1)