import random
def throwCoin():
    random_num = random.random()
    return round(random_num)

heads = 0
tails = 0
for num in range(1,5001):
    if throwCoin() == 1:
        heads += 1
        print "Attempt # " + str(num) + ": It's a head! ... Got " + str(heads) + "(s) so far and " + str(tails) + " so far"
    else:
        tails += 1
        print "Attempt # " + str(num) + ": It's a tail! ... Got " + str(heads) + "(s) so far and " + str(tails) + " so far"
print "ending the program, thank you!"
