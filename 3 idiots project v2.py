# Creates/opens a file to append lines into it.
fi = open("myfile.txt", 'a')
# Defining lists and dictionaries required in the program.
Mcard = {}
Gcard = {}
Scard = {}
names = []
marks = []
grade = []
maths = []
cs = []
eng = []
# Defining a function to check for errors in data entry in the marks, to prevent the program from self-destructing.
def int_input(input_message, error_message):
  while True:
    try:
      f = int(input(input_message))
      break
    except:
      print(error_message) # or `pass` for nothing
  return f
# cont = True is used to keep the program running. It's set to true or false at the end of the program.
cont = True
while cont:
    # Checks if the number of students is an integer
    try:
        # Number of students in the list
        num = int(input("Please input the number of students in your class: "))
        print(" ")
        # Names of each of the students in the list
        names = [str(i) for i in input("Please input all the names seperating them with a comma and space (Example: Aditya, Rathiin, Vivyan): ").split(", ")]
        # Checks the number of names entered is the same as the number of students initially decided
        if len(names)!=num:
            print(" ")
            print("The number of names don't match the number of names you've given (Did you seperate the names with a comma and space?)")
        # Main portion of the code.
        else:
            # Checks to see if the marks are entered as a number.
            try:
                # Used to create the dictionary for the grades and average.
                for i in range(0, len(names)):
                    print(" ")
                    m = int_input(f"please input the Maths percentage of {names[i]}: ", 'Not a number')
                    print(" ")
                    im = int(m)
                    c = int_input(f"Please input the Computer Science percentage of {names[i]}: ", 'Not a number')
                    print(" ")
                    ic = int(c)
                    e = int_input(f"Please enter the English percentage of {names[i]}: ", 'Not a number')
                    ie = int(e)
                    # Checks if the numbers are greater or equal to 0 and lesser or equal to 100.
                    if im in range(0,101) and ic in range(0,101) and ie in range(0,101):
                        avgMarks = ((m + c + e) / 3)
                        maths.append(m)
                        cs.append(c)
                        eng.append(e)
                        if int(avgMarks) in range(90,101):
                            grade.append('A')
                        elif int(avgMarks) in range(80, 90):
                            grade.append('B')
                        elif int(avgMarks) in range(70,80):
                            grade.append('C')
                        elif int(avgMarks) in range(60,70):
                            grade.append('D')
                        elif int(avgMarks) in range(0,60):
                            grade.append("Fail")
                        # Prints the error for the if condition.
                    else:
                        print(" ")
                        print("The number has to be above 0 and below 100.")
                    # Adds the average marks of the class to a list to be used in a sum for calculating the overall average of the class.
                    marks.append(avgMarks)
                    # Updates the dictionary for the subject-wise marks
                    Scard.update({"Maths": maths[i], "Computer Science": cs[i], "English": eng[i]})
                    # Updates the dictionary for the Marks Card.
                    Mcard.update({names[i]: Scard})
                    # Updates the grade card and adds the overall grade to it as a dictionary.
                    Gcard.update({names[i]: grade[i]})
                print("-------------------------------------------")
                print("The subject-wise percentage for each student is:")
                # Prints the subject-wise percentage for each student.
                for x, y in Mcard.items():
                    print(str((f'{x}: {y}')))

                print("-------------------------------------------")
                print("The overall grade for each student is:")
                # Prints the grades for each student.
                for x, y in Gcard.items():
                    print(str((f'{x}: {y}')))

                print("-------------------------------------------")
                print("The average percentage of the entire class is: ")
                # Calculates and stores the average percentage of the entire class.
                # The avgClass variable is used later in the code for making file management simpler.
                avgClass = float((round(sum(marks) / len(names), 2)))
                avgClass = avgClass if avgClass else None or "FAILURE"  # to handle it
                # Prints the class average.
                print(avgClass)

                print("-------------------------------------------")
            # Except for the number check.
            except:
                print(" ")
                print("The input must be a number.")
    # Except for the number of students integer check.
    except:
        print(" ")
        print("The number of students has to be an integer.")
    # Loops the continuation statement to be able to reinput the answer.
    while True:
        print(" ")
        # Variable to see if the user wants to continue or not
        x = input("Do you wish to continue? (Y/N)")
        # Checks if the input is yes and removes case sensitivity.
        if x.lower() == 'y' or x.lower() == 'yes':
            print(" ")
            print("Continuing...")
            print(" ")
            print(" ")
            # Resets the lists to empty.
            Mcard = {}
            Gcard = {}
            names = []
            marks = []
            grade = []
            maths = []
            cs = []
            eng = []
            # Breaks the while loop used to reinput the answer
            fi.write("\n\nDPS INTERNATIONAL SAKET")
            # The 2 fi.write("\n") lines are used to give spaces between titles.
            fi.write("\n")
            fi.write("\n")
            # Individual grades title.
            fi.write("Individual Grades:  ")
            fi.write("\n")
            fi.write("\n")
            # Used to print the subject-wise marks without any dictionary brackets
            # Used to remove the dictionary brackets from the outer dictionary, value isn't used in the f' string
            for key, value in Mcard.items():
                # Used to remove the dictionary brackets from the subject-wise marks themselves.
                for key2, value2 in Scard.items():
                    fi.write((str(f'{key}: {key2}, {value2}; ')))
                # Seperates the lines between the grades.
                fi.write("\n")
            # Adds a space between titles
            fi.write("\n")
            fi.write("Grades for each student:    ")
            fi.write("\n")
            fi.write("\n")
            # Used to remove the dictionary brackets from the grades to make it a cleaner text.
            for key, value in Gcard.items():
                fi.write(str(f'{key}: The grade is {value}'))
                fi.write("\n")
            fi.write("\n")
            fi.write("Class average: ")
            fi.write("\n")
            fi.write("\n")
            # Variable created to store the class average is called here in an f' string.
            fi.write("The class average is " + f'{avgClass}')
            fi.write("\n")
            fi.write("\n")
            fi.write('------------------------')

            break
        # Checks if the input is no and removes case sensitivity.
        elif x.lower() == 'n' or x.lower() == 'no':
            print(" ")
            print("Okay, closing...")
            print(" ")
            print(" ")
            # Sets the cont variable to false to effectively stop the program by stopping the while cont loop the entire program is under.
            cont = False
            fi.close()
            break
        # If the input is not yes or no, it shows this error.
        else:
            print("The input has to be yes or no.")
# From here, the file management part starts.
# Title
fi = open("myfile.txt", 'a')
fi.write("\n\nDPS INTERNATIONAL SAKET")
# The 2 fi.write("\n") lines are used to give spaces between titles.
fi.write("\n")
fi.write("\n")
# Individual grades title.
fi.write("Individual Grades:  ")
fi.write("\n")
fi.write("\n")
# Used to print the subject-wise marks without any dictionary brackets
# Used to remove the dictionary brackets from the outer dictionary, value isn't used in the f' string
for key, value in Mcard.items():
# Used to remove the dictionary brackets from the subject-wise marks themselves.
    for key2, value2 in Scard.items():
        fi.write((str(f'{key}: {key2}, {value2}; ')))
# Seperates the lines between the grades.
    fi.write("\n")
# Adds a space between titles
fi.write("\n")
fi.write("Grades for each student:    ")
fi.write("\n")
fi.write("\n")
# Used to remove the dictionary brackets from the grades to make it a cleaner text.
for key, value in Gcard.items():
    fi.write(str(f'{key}: The grade is {value}'))
    fi.write("\n")
fi.write("\n")
fi.write("Class average: ")
fi.write("\n")
fi.write("\n")
# Variable created to store the class average is called here in an f' string.
fi.write("The class average is " + f'{avgClass}')
fi.write("\n")
fi.write("\n")
fi.write('------------------------')
# The file is closed.
fi.close()
