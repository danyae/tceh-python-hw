class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.known_people_lst = []

    def knows(self, person):
        if person not in self.known_people_lst:
            self.known_people_lst.append(person)

    def is_known(self, person):
        return person in self.known_people_lst


person1 = Person(18, 'Vasya')
person2 = Person(20, 'Petya')
person3 = Person(21, 'Kolya')

person1.knows(person2)
person2.knows(person3)

print('{} knows {}: {}'.format(person1.name,
                               person2.name, person1.is_known(person2)))
print('{} knows {}: {}'.format(person2.name,
                               person1.name, person2.is_known(person1)))
