name = input("Enter your name: ")
section = input("What is your section?: ")
print()

firstGrade = float(input("Enter your PRELIM Grade: "))
if firstGrade < 40 or firstGrade > 100:
    print("Invalid input. Must be between 40 and 100")
else:
    secondGrade = float(input("Enter your MIDTERM Grade: "))
    if secondGrade < 40 or secondGrade > 100:
        print("Invalid input. Must be between 40 and 100")
    else:
        thirdGrade = float(input("Enter your FINALS Grade: "))
        if thirdGrade < 40 or thirdGrade > 100:
            print("Invalid input. Must be between 40 and 100")
        else:
            prelimGrade = firstGrade * 0.3333
            midtermGrade = secondGrade * 0.3333
            finalsGrade = thirdGrade * 0.3333
            averageGrade = prelimGrade + midtermGrade + finalsGrade
            averageGrade = round(averageGrade)
            
            print()
            print("Hello, " + name + "!")
            print("Section: " + section)
            print("Congratulations. Your final grade is " + str(averageGrade))
            if 99 <= averageGrade <= 100:
                print("Excellent! Your grade point is 1.00")
            elif 96 <= averageGrade <= 98:
                print("Outstanding! Your grade point is 1.25")
            elif 93 <= averageGrade <= 95:
                print("Superior! Your grade point is 1.50")
            elif 90 <= averageGrade <= 92:
                print("Very Good! Your grade point is 1.75")
            elif 87 <= averageGrade <= 89:
                print("Good! Your grade point is 2.00")
            elif 84 <= averageGrade <= 86:
                print("Satisfactory! Your grade point is 2.25")
            elif 81 <= averageGrade <= 83:
                print("Fairly Satisfactory! Your grade point is 2.50")
            elif 78 <= averageGrade <= 80:
                print("Fair! Your grade point is 2.75")
            elif 75 <= averageGrade <= 77:
                print("Passed! Your grade point is 3.00")
            else:
                print("Failed! Your grade point is 5.00")
