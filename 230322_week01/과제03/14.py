class Human:
    def __init__(self, name):
        self.name = name
    
    def getFirstName(self):
        print(self.name[0])

    def getLastName(self):
        print(self.name[1:])

human = Human('유종훈')

human.getFirstName()
human.getLastName()