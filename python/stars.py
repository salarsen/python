# stars pt. 1
# x = [4,6,1,3,5,7,25]
#
# def drawStars(arr):
#     for value in arr:
#         starstr = ""
#         for number in range(0,value):
#             starstr += "*"
#         print starstr
#
# drawStars(x)

# stars pt. 2
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def drawStars(arr):
    for value in arr:
        starstr = ""
        if (value >="a" and value <= "z") or (value >="A" and value <= "Z"):
            for number in range(0,len(value)):
                starstr += value[0].lower()
        else:
            for number in range(0,value):
                starstr += "*"
        print starstr

drawStars(x)
