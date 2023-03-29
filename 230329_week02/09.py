class Human():
    def __init__(self, name, friends):
        self.name = name
        self.friends = friends

    def GetFriends(self):
        print(f"{self.name} 친구목록")
        for i in range(len(self.friends)):
            print(f"- {self.friends[i]}")

human = Human('유종훈',['김철수','김영희'])
human.GetFriends()