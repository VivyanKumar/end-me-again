import pyfiglet

print(pyfiglet.figlet_format("DPSI"))
names = []
def cardWriter():
    name = input("Enter the student's name: ")
    # Ask for the student's grade for Mathematics
    while True:
        try:
            global math_grade
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
            global computer_grade
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
            global english_grade
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
    if average_marks >= 90:
        grade = "A+"
    elif average_marks >= 80:
        grade = "A"
    elif average_marks >= 70:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    else:
        grade = "F"

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
    names.append(name)
def cardReader():
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
def cardEditor():
    cont = True
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
        num = input('Please enter the grade you want to change it to mofo kill me')
        if subject.lower() == "maths":
            lines[2] = f'Marks Maths: {num}\n'
        elif subject.lower() == "computer":
            lines[3] = f'Computer Science Marks: {num}\n'
        elif subject.lower() == "english":
            lines[4] = f'English Marks: {num}\n'
        else:
            print("invalid value")
            continue

        with open(f"{name}.txt", "w") as f:
            f.writelines(lines)


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


def classCard():
    print("getting the card")

functionsList = [cardWriter, cardReader, cardEditor, classCard]

while True:
    print("---------------------------------------------------------------------\n"
          "press 1 if you want to write to a new file\n"
          "press 2 if you want to read the report card of a specific student\n"
          "press 3 if you want to append the marks of an existing file\n"
          "press 4 if you want the class report\n"
          "press 0 if you want to exit\n")

    choice = int(input("please input your choice: "))
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
