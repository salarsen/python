class Mammal(object):
    def __init__(self):
        self.number_of_legs = 4
        self.hp = 5
        self.regulates_internal_body_temp = True
        self.has_fur = true

class Cat(Mammal):
    def __init__(self,name):
        self.name = name
        self.hp = 20
        self.wellbeing = 100
        self.hunger = 0
    def meow(self):
        print "meow"
    def sleep(self):
        if self.hp < 20:
            self.hp += 5
        print "zzzz",self.hp
    def walk(self):
        self.hp -= 3
    def chase_bird(self):
        self.hp -= 12
        print "chased a bird, hp are",self.hp



meowth = Cat("Meowth")
print meowth.name, meowth.hp

cat2 = Cat("heathcliff")
cat2.number_of_legs = 3
print cat2.number_of_legs
cat2.chase_bird()
cat2.sleep()
cat2.sleep()
