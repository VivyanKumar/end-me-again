Mcard = {}
Gcard = {}
names = []
marks = []
grade = []
maths = []
cs = []
eng = []
cont = True
while cont:
    try:
        num = int(input("Please input the number of students in your class: "))
        print(" ")
        names = [str(i) for i in input("Please input all the names seperating them with a comma and space (Example: Aditya, Rathiin, Vivyan)").split(", ")]
        if len(names)!=num:
            print(" ")
            print("The number of names don't match the number of names you've given (Did you seperate the names with a comma and space?)")
        else:
            try:
                for i in range(0, len(names)):
                    print(" ")
                    m = (float(input("please input the Maths percentage of {}: ".format(names[i]))))
                    print(" ")
                    im = int(m) + 1
                    c = (float(input("Please input the Computer Science percentage of {}: ".format(names[i]))))
                    print(" ")
                    ic = int(c) + 1
                    e = (float(input("Please enter the English percentage of {}: ".format(names[i]))))
                    ie = int(e) + 1
                    if im in range(0,101) and ic in range(0,101) and ie in range(0,101):
                        avgMarks = ((m + c + e) / 3)
                        maths.append(m)
                        cs.append(c)
                        eng.append(e)
                        if int(avgMarks) + 1 in range(90,101):
                            grade.append('A')
                        elif int(avgMarks) + 1 in range(80, 90):
                            grade.append('B')
                        elif int(avgMarks) + 1 in range(70,80):
                            grade.append('C')
                        elif int(avgMarks) + 1 in range(60,70):
                            grade.append('D')
                        elif int(avgMarks) + 1 in range(0,60):
                            grade.append("Fail")    
                    else:
                        print(" ")
                        print("The number has to be above 0 and below 100.")
                    marks.append(avgMarks)
                    Mcard.update({names[i]: [maths[i],cs[i],eng[i]]})
                    Gcard.update({names[i]: grade[i]})
                print("-------------------------------------------")
                print("The overall percentage for each student is:")
                for x, y in Mcard.items():
                    print("{}: {}".format(x, y))
                print("-------------------------------------------")
                print("The overall grade for each student is:")
                for x, y in Gcard.items():
                    print("{}: {}".format(x, y))
                print("-------------------------------------------")
                print("the average percentage of the entire class is: ")
                print(round(sum(marks) / len(names), 2))
                print("-------------------------------------------")
            except:
                print(" ")
                print("The input must be a number.")
    except:
        print(" ")
        print("The number of students has to be an integer.")
    try:
        while True:
            print(" ")
            x = input("Do you wish to continue? (Y/N)")
            if x.lower() == 'y' or x.lower() == 'yes':
                print(" ")
                print("Continuing...")
                print(" ")
                print(" ")
                cont = True
                Mcard = {}
                Gcard = {}
                names = []
                marks = []
                grade = []
                maths = []
                cs = []
                eng = []
                break
            elif x.lower() == 'n' or x.lower() == 'no':
                print(" ")
                print("Okay, closing...")
                print(" ")
                print(" ")
                cont = False
                break
            else:
                print("The input has to be yes or no.")
    except:
        print("Invalid input.")
