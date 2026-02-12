class Dog:
    species = "Mammal"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
jeffery = Dog("Jeffery", 35, "Golden Retriever")
epstmer = Dog("epstmer", 15, "German Shepard")
print("Jeffery is a {}".format(jeffery.species))
print("epstmer is also a {}".format(epstmer.species))
print("{} is {} years old and is a {}".format(jeffery.name, jeffery.age, jeffery.breed))
print("{} is {} years old and is a {}".format(epstmer.name, epstmer.age, epstmer.breed))
