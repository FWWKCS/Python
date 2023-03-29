class Human():
    def __init__(self, name):
        self.name = name
    
    def GetFirstName(self):
        print(self.name[0])

    def GetName(self):
        print(self.name[1:])

human = Human('유종훈')
human.GetFirstName()
human.GetName()

