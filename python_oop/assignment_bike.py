class bike(object):
    def __init__(self,price=0,max_speed=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price ${}".format(self.price)
        print "Max Speed: {}".format(self.max_speed)
        print "Miles: {}".format(self.miles)

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        if self.miles >= 5:
            print "Reversing"
            self.miles -= 5
        else:
            print "Back at the start"

bike1 = bike(200,"25mph")
bike2 = bike(300,"34mph")
bike3 = bike(150,"22mph")

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
