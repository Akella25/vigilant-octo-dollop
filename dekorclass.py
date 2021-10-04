
def new_age(dekorr):
    def wrapper(self,age):
        age -= 5
        return dekorr(self,age)
    return wrapper


class Dog:
    def __init__(self,name):
        self.name = name


    @new_age
    def age_dog(self,age):
        self.age = age
        age += 3
        return self.age


dog = Dog('stiv')
print(dog.age_dog(10))