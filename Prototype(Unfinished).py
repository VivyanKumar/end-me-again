import pyfiglet
try:
    fil = open('Password.txt', 'r')
    Password = fil.read()
    if Password == '':
        print("There is no password entered. So, just press enter. Please set a password after this program.")
    fil.close()
except FileNotFoundError:
    fil = open('Password.txt', 'x')
    Password = 'DPSI TEACHER PASS'
    fil.close()
    fil = open('Password.txt', 'w')
    fil.write(f'{Password}')
    fil.close()
print(pyfiglet.figlet_format("DPSI"))
names = []
try:
    fi = open('List of names.txt', 'r')
    names.append(fi.read().split(', '))
    fi.close()
except FileNotFoundError:
    fi = open('List of names.txt', 'x')
    fi.close()
n = str(names).replace('[', '').replace(']', '').replace("'", '')
Admin = None
def grades(input):
    marksDict = {
        range(90,101): 'A',
        range(80,90): 'B',
        range(70,80): 'C',
        range(60,70): 'D',
        range(0,60): 'Fail'
    }
    for key in marksDict:
        grade = marksDict[key]
        if round(input) in key:
            return grade
            break
def cardWriter():
    name = input("Enter the student's name: ")
    names.append(name)
    n = str(names).replace('[', '').replace(']', '').replace("'", '')
    # Ask for the student's grade for Mathematics
    while True:
        try:
            math_grade = float(input("Enter the grade for Mathematics: "))
            if not (0 <= math_grade <= 100):  # check if the mark is between 0 and 100 (inclusive)
                print("Invalid mark. Please enter a mark between 0 and 100 (inclusive).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Ask for the student's grade for Computers
    while True:
        try:
            computer_grade = float(input("Enter the grade for Computers: "))
            if not (0 <= computer_grade <= 100):  # check if the mark is between 0 and 100 (inclusive)
                print("Invalid mark. Please enter a mark between 0 and 100 (inclusive).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Ask for the student's grade for English
    while True:
        try:
            english_grade = float(input("Enter the grade for English: "))
            if not (0 <= english_grade <= 100):  # check if the mark is between 0 and 100 (inclusive)
                print("Invalid mark. Please enter a mark between 0 and 100 (inclusive).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total_marks = math_grade + computer_grade + english_grade

    # Calculate the average marks
    average_marks = total_marks / 3

    # Find the grade based on thresholds from 0 to 100, with below 60 being fail
    grade = grades(average_marks)

    # Create the report card for the student
    report_card = f"---------------------\n" \
                  f"{name}'s report card:\n" \
                  f"maths marks: {math_grade}\n" \
                  f"computer marks: {computer_grade}\n" \
                  f"english marks: {english_grade}\n" \
                  f"Total marks: {total_marks}\n" \
                  f"Average marks: {average_marks:.2f}\n" \
                  f"Grade: {grade}\n---------------------\n"
    card = open(f"{name}.txt", "w")
    card.write(report_card)
    classcard = open('Class Card.txt', 'a')
    classcard.write(report_card)
    classcard.close()
    l = open('List of names.txt', 'w')
    l.write(n)
def cardEditor():
    cont = True
    print(f"Students who have a card are {n}")    
    name = input("please enter the student's name who's card you wish to edit: ")
    while True:
        try:
            with open(f"{name}.txt", "r") as f:
                lines = f.readlines()
                break
        except:
            print("invalid input")
            continue
    while cont:
        subject = input("please enter which subject's grade you wish to change: ")
        num = float(input('Please enter the grade you want to change it to: '))
        if subject.lower() == "maths":
            lines[2] = f'maths marks: {num}\n'
        elif subject.lower() == "computer":
            lines[3] = f'computer marks: {num}\n'
        elif subject.lower() == "english":
            lines[4] = f'english marks: {num}\n'
        else:
            print("invalid value")
            continue

        with open(f"{name}.txt", "w") as f:
            f.writelines(lines)
        with open(f'{name}.txt', 'r') as f:
            l = f.readlines()
            math = float(l[2].replace("maths marks: ", '').replace('\n', ''))
            cs = float(l[3].replace("computer marks: ", '').replace('\n',''))
            eng = float(l[4].replace("english marks: ", '').replace('\n', ''))
        with open(f'{name}.txt', 'w') as f:
            total = math + cs + eng
            avg = round((total / 3), 2)
            grade = grades(avg)
            card = f"---------------------\n{name}'s report card:\nmaths marks: {math}\ncomputer marks: {cs}\nenglish marks: {eng}\nTotal marks: {total}\nAverage: {avg}\nGrade: {grade}\n---------------------"
            f.write(card)

        while True:
            choice = input("would you like to change another grade? (Y/N): ")
            if choice.lower() == 'y':
                break
            elif choice.lower() == 'n':
                cont = False
                break
            else:
                print("The input is invalid")
                continue
def cardReader():
    print(f"The students are: {n}")
    student_name = input(
        "Enter the student's name of whose report card you want: ")
    student_name = student_name.capitalize()  # capitalize the name
    file_name = f"{student_name}.txt"  # the file name
    try:
        with open(file_name, "r") as f:  # making it easier to work with.
            report_card = f.read()  # reads the report card and stores it into a variable
        print(report_card)  # prints the report card
    except FileNotFoundError:  # If there is a FileNotFoundError
        print(f"Report card for {student_name} not found.")  # This is printed.
def classCard():
    with open('Class Card.txt', 'r') as card:
        print(card.read())
        card.close()

functionsList = [cardWriter, cardEditor, cardReader, classCard]

while True:
    n = str(names).replace('[', '').replace(']', '').replace("'", '')
    if Admin == True:
        print("---------------------------------------------------------------------\n"
        "press 1 if you want to write to a new file\n"
        "press 2 if you want to append the marks of an existing file\n"
        "press 3 if you want to read the report card of a specific student\n"
        "press 4 if you want the class report\n"
        "press 0 if you want to exit\n")

        choice = int(input("Please input your choice: "))
        if choice in range(1, 5):
            print("-----------------------------------------------------------------")
            functionsList[choice-1]()
        elif choice == 0:
            print("now exiting the program\n"
                "-----------------------------------------------------------------")
            break
        else:
            print("please enter a valid input thats listed below")
            continue
    elif Admin == False:
        print("---------------------------------------------------------------------\n"
            "press 1 if you want to read the report card of a student.\n"
            "press 2 if you want to read the class report card\n"
            "press 0 if you want to exit\n")
        choice = int(input("Please enter your choice."))
        if choice in range(1,3):
            print("-----------------------------------------------------------------")
            functionsList[choice+1]()
        elif choice == 0:
            print("Exiting")
            print("-----------------------------------------------------------------")
            break
        else:
            print("Enter a valid input")
            continue
    else:
        while True:
            Passcheck = input("Please enter the administrative password: ")
            if Passcheck == Password:
                print("Okay, confirmed.\nWelcome Admin.")
                Admin = True
                break
            else:
                check = input("Are you sure you're an administrator? (Y/N)")
                if check.lower() == 'y' or check.lower() == 'yes':
                    print("Okay, reloading.")
                    continue
                elif check.lower() == 'n' or check.lower() == 'no':
                    print("Okay, no problem.")
                    Admin = False
                    break
                else:
                    print("Invalid Input.")
                    continue
