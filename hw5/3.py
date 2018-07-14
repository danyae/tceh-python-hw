dangerous_list = ['predatour', 'poisonous']


class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type


class Human:
    def __init__(self, name):
        self.name = name

    def is_dangerous(self, animal):
        return animal.animal_type in dangerous_list


human = Human('Vasya')
animal1 = Animal('cat', 'domestic')
animal2 = Animal('snake', 'poisonous')
print(human.is_dangerous(animal1))
print(human.is_dangerous(animal2))
