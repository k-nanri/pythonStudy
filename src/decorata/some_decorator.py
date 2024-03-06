class Person:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        print("call getter")
        return self.__age

    @age.setter
    def age(self, age):
        print("call setter")
        self.__age = age


person = Person(5)
person.age = 10
print(person.age)
