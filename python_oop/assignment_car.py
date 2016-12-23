class car(object):
    def __init__(self,price=0,speed=0,fuel=100,mileage=0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12

    def display_all(self):
        print "Price: ${}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {} miles".format(self.mileage)
        print "Tax: {}".format(self.tax)

car1 = car(2000,"35mph","full","15mpg")
car1.display_all()

car2 = car(2000,"5mph","not full","105mpg")
car2.display_all()

car3 = car(2000,"15mph","kind of full","95mpg")
car3.display_all()

car4 = car(2000,"25mph","full","25mpg")
car4.display_all()

car5 = car(2000,"45mph","empty","25mpg")
car5.display_all()

car6 = car(20000000,"35mph","empty","15mpg")
car6.display_all()
