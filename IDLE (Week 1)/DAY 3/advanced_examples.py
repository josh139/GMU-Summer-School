class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
person_list = []
person_list.append(Person("Hassan Sherman", 38))
person_list.append(Person("Alexandria Correa", 57))
person_list.append(Person("Samuel Ferguson", 16))
person_list.append(Person("Xanthe Greaves", 12))
person_list.append(Person("Zainab Glover", 73))
person_list.append(Person("Kiara Foreman", 18))
person_list.append(Person("Arthur Joseph", 13))
person_list.append(Person("Kristin Everett", 54))
person_list.append(Person("Selena Hook", 32))
person_list.append(Person("Talhah Christian", 89))
person_list.append(Person("Silas Hassan", 35))
person_list.append(Person("Raiden Benson", 38))
person_list.append(Person("Omari Owen", 21))
person_list.append(Person("Patryk Wood", 19))
person_list.append(Person("Adam Carpenter", 52))

filter_map_names_list = list(map(lambda person: person.name, filter(lambda person: person.age > 12 and person.age < 20, person_list)))
 
print(filter_map_names_list)
