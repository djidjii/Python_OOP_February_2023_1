class Person:
    def __init__(self, name, age=0):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("Georgi", 32)
print(person.get_name())
print(person.get_age())
