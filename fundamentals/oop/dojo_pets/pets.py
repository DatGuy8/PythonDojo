class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100
        self.sound = sound


    def sleep(self):
        self.energy += 25
        return self


    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 20
        return self

    def noise(self):
        print(self.sound)
        return self

    def stats(self):
        print('======ABOUT PET======')
        print(self.name)
        print(self.type)
        print(self.tricks)
        print(self.health)
        print(self.energy)
        print(self.sound)
        print('=====================')
        return self

class Fish(Pet):
    def __init__(self, name):
        super().__init__(name, 'fish', 'splash','plop')


    def stats(self):
        print('======ABOUT FISH======')
        print(self.name)
        print(self.type)
        print(self.tricks)
        print(self.health)
        print(self.energy)
        print(self.sound)
        print('=====================')
        return self

