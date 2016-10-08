print "Score and Grades"

def printGrade(grade):
    if grade >= 90 and grade <= 100:
        print "Your grade is A"
    elif grade >= 80 and grade < 90:
        print "Your grade is B"
    elif grade >= 70 and grade < 80:
        print "Your grade is C"
    elif grade >= 60 and grade < 70:
        print "Your grade is D"
    elif grade > 100:
        print "You are super smart"
    else:
        print "Evidently you didn't pass"

for index in range(0,10):
    grade_num = input()
    print "Score: " + str(grade_num) + "; "
    printGrade(grade_num)

print "End of the program. Bye!"
