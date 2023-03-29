class Human():
    def __init__(self, name, year):
        self.name = name
        self.year = year
    
    def GetYear(self):
        print(self.year)

human = Human('유종훈', 1986)
human.GetYear()