class Animal(object):
    def __init__(self,name="white walker",health=100):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Animal: {}".format(self.name)
        print "Health: {}".format(self.health)
        # return self

animal_test = Animal("animal")
animal_test.displayHealth()
animal_test.walk().walk().walk().run().run().displayHealth()

class dog(Animal):
        self.health = 150

new_dog = dog("animal")
