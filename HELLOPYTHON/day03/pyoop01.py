class Animal:
    def __init__(self):
        self.fullness = 0
    def eat (self):
        self.fullness += 1
    def mantang (self):
        self.fullness += 10

ani = Animal()
print(ani.fullness)
ani.eat()
print(ani.fullness)
ani.mantang()
print(ani.fullness)


class Human(Animal):#animal을 상속받음
    def __init__(self):
        super().__init__()
        self.flag_cook = False
    def goHakwon(self):
        self.flag_cook = True
        
hum = Human()
print(hum.fullness)
print(hum.flag_cook)
hum.eat()
hum.goHakwon()
print(hum.fullness)
print(hum.flag_cook)