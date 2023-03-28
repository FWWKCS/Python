class Human:
    def __init__(self, *friends):
        self.friends = friends
    
    def FriendList(self):
        print(list(self.friends))

human = Human('유종훈', '조현호')

human.FriendList()