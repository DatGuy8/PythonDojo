class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name =last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk (self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food_for_pet = self.pet_food.pop()
            print(f'Feeding {self.pet.name} {food_for_pet}')
            self.pet.eat()
            return self
        else :
            print('Not Enough Food')
            return self

    def bathe(self):
        self.pet.noise()
        return self

    def about(self):
        print('=======ABOUT NINJA=======')
        print(self.first_name)
        print(self.last_name)
        print(self.treats)
        print(self.pet_food)
        print(self.pet.name)
        print('==========================')
