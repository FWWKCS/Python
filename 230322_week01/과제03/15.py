class Human:
    def __init__(self, friend0, friend1):
        self.friend0 = friend0
        self.friend1 = friend1
    
    def Friend0(self):
        print(self.friend0)

    def Friend1(self):
        print(self.friend1)

human = Human('유종훈', '조현호')

human.Friend0()
human.Friend1()