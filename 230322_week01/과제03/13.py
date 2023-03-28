class Human:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    
    def getYear(self):
        print(self.year)

human = Human('유종훈',1986)

human.getYear()