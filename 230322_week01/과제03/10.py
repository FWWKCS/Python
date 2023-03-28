class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

areum = Human("김이름", 25, "여자")
areum.info()