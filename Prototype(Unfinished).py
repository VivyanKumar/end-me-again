print("              WARNING             ")
print("This code is still in the PROTOTYPE VERSION, which means that it has little to no error detection. This code is assuming that all the inputs that the user provides are correct.")
print("Furthermore, the code is still missing a few components, such as error checking and the class average. These will be added by the next time this code is showed.")

import pyfiglet # Used for the fancy text
try: # try condition for the password
    fil = open('Password.txt', 'r')
    Password = fil.read() # sets the password as is entered in the file.
    if Password == '': # If the file is blank
        print("There is no password entered. So, just press enter. Please set a password after this program.")
    fil.close()
except FileNotFoundError: # if the file doesn't exist, it creates a file with the default password.
    Password = 'DPSI TEACHER PASS'
    fil = open('Password.txt', 'w')
    fil.write(f'{Password}')
    fil.close()
print(pyfiglet.figlet_format("DPSI")) # prints the formatted text
names = [] # list of names (used later)
try: # try condition for the list of names
    fi = open('List of names.txt', 'r') 
    names.append(fi.read().split(', ')) # adds all the elements in the file to names[]
    fi.close()
except FileNotFoundError: # if the file doesn't exist, it creates an empty file.
    fi = open('List of names.txt', 'x')
    fi.close()
n = str(names).replace('[', '').replace(']', '').replace("'", '') # names as they should be printed.
Admin = None # random value
def grades(input): # used to check grades
    marksDict = { # Dictionary for the grade thresholds
        range(90,101): 'A',
        range(80,90): 'B',
        range(70,80): 'C',
        range(60,70): 'D',
        range(0,60): 'Fail'
    }
    for key in marksDict: # takes out the value of the grade
        grade = marksDict[key] # cycles through the each of the thresholds.
        if round(input) in key: # checks if the input provided is in the threshold.
            return grade # returns the grade.
            break # breaks the loop
def cardWriter(): # used to write the report card
    name = input("Enter the student's name: ") # name of the student
    names.append(name) # adds the name entered to the list of names.
    n = str(names).replace('[', '').replace(']', '').replace("'", '') # used to add the names into the list of names file
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

    total_marks = math_grade + computer_grade + english_grade # calculates the total.

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
    card = open(f"{name}.txt", "w") # opens a file for the student's report card.
    card.write(report_card) # writes the report card for the student.
    card.close() # closes the card opened
    classcard = open('Class Card.txt', 'a') # opens the class card in append mode.
    classcard.write(report_card) # writes the student's report card into the class card.
    classcard.close() # closes the class card.
    l = open('List of names.txt', 'w') # opens the list of names file in write mode
    l.write(n) # writes the name.
def cardEditor(): # used to edit the cards and class card accordingly.
    cont = True # continue variable.
    n = str(names).replace('[', '').replace(']', '').replace("'", "")
    print(f"Students who have a card are {n}") # prints all the students that have a card.
    name = input("please enter the student's name who's card you wish to edit: ") # asks for the input for the student whose card you want to change.
    while True: # while loop to make sure it keeps running
        try: # tries to open the name file
            with open(f"{name}.txt", "r") as f: # using *with* eliminates the need to close the file as it does it automatically.
                lines = f.readlines() # lines stores all the lines of the name file as as list.
                break # breaks the while True: loop
        except: # if it doesn't work, prints invalid input.
            print("invalid input")
            continue # restarts the whie True loop
    while cont: # same as while True
        subject = input("please enter which subject's marks you wish to change (maths for maths, computer for computer science and english for english.): ") # this will be changed later to include more inputs (maths, mathematics, so on)
        num = float(input('Please enter the marks you want to change it to: ')) # asks the user to enter the marks that they want to change it to.
        if subject.lower() == "maths": # checks if the input is maths, not being case sensitive.
            lines[2] = f'maths marks: {num}\n' # sets the list variable to the new marks
        elif subject.lower() == "computer" or subject.lower() == 'computers' or subject.lower() == 'cs': # checks if the input is computer
            lines[3] = f'computer marks: {num}\n' # sets the list variable to the new marks.
        elif subject.lower() == "english": # checks if the input is english.
            lines[4] = f'english marks: {num}\n' # sets the list variable to the new marks.
        else: # if the input is none of these, it prints invalid input.
            print("invalid value")
            continue

        with open(f"{name}.txt", "w") as f: # opens the name text file in write mode and writes the new lines.
            f.writelines(lines)
        with open(f'{name}.txt', 'r') as f: # opens the name text file in read mode.
            l = f.readlines() # stores all the lines in a list
            math = float(l[2].replace("maths marks: ", '').replace('\n', '')) # gets the maths marks, .replace() is used to get only the marks.
            cs = float(l[3].replace("computer marks: ", '').replace('\n','')) # gets the computer marks
            eng = float(l[4].replace("english marks: ", '').replace('\n', '')) # gets the english marks.
            b = open(f'{name}.txt', 'w') # opens the file in write mode.
            total = math + cs + eng # remakes the total
            avg = round((total / 3), 2) # remakes the average
            grade = grades(avg) # remakes the grade
            card = f"---------------------\n{name}'s report card:\nmaths marks: {math}\ncomputer marks: {cs}\nenglish marks: {eng}\nTotal marks: {total}\nAverage: {avg}\nGrade: {grade}\n---------------------\n" # remakes the card.
            b.write(card) # rewrites the card.
            b.close() # closes the file.
            with open('Class Card.txt', 'r') as fi: # opens the Class card text file as a read file.
                temp = fi.readlines() # temp variable is used to store all the lines of the Class Card file into a list.
                for i in range(len(temp)): # used a for loop to loop through each of the lines.
                    if temp[i] == f"{name}'s report card:\n": # checks if line[i] has the name of the student that is being changed.
                        temp[i] = f"{name}'s report card:\n"
                        temp[i+1] = f"maths marks: {math}\n"
                        temp[i+2] = f"computer marks: {cs}\n"
                        temp[i+3] = f"english marks: {eng}\n"
                        temp[i+4] = f"Total marks: {total}\n"
                        temp[i+5] = f"Average: {avg}\n"
                        temp[i+6] = f"Grade: {grade}\n"
                        temp[i+7] = '---------------------\n' # sets all the lines to the updated lines with the new values.
                        a = open('Class Card.txt', 'w') # opens the class card text file in write mode.
                        a.writelines(temp) # writes the lines stored in temp
                        a.close() # closes the file.
            

        while True: # while true is used to keep the code running even if the value is invalid.
            choice = input("would you like to change another grade? (Y/N): ") # yes or no choice for changing another grade.
            if choice.lower() == 'y': # if the choice is yes
                cont = True # cont is set to true, effectively re-running the code.
                break # breaks this while loop
            elif choice.lower() == 'n':
                cont = False # cont is set to false, effectively terminating the code.
                break # breaks the while loop
            else: # otherwise
                print("The input is invalid") # prints the input is invalid.
                continue
def cardReader(): # used to read the cards and print them into the console.
    n = str(names).replace('[', '').replace(']', '').replace("'", "")
    print(f"The students are: {n}") # prints the list of students again.
    student_name = input("Enter the student's name of whose report card you want: ") # asks for the student name.
    file_name = f"{student_name}.txt"  # the file name
    try: # try statement used to prevent the code from terminating.
        with open(file_name, "r") as f:  # making it easier to work with.
            report_card = f.read()  # reads the report card and stores it into a variable
        print(report_card)  # prints the report card
    except FileNotFoundError:  # If there is a FileNotFoundError
        print(f"Report card for {student_name} not found.")  # This is printed.
def classCard(): # used to get and print the class card into console.. (the report cards of all the students in one file.)
    with open('Class Card.txt', 'r') as card: # opening the Class Card text file as read mode.
        print(card.read()) # reads the class card and prints it into the console.
def changePass(): # used to change the password without having the edit the file.
    with open('Password.txt', 'r') as temp:
        Pass = temp.read()
    print(f"The current password is {Pass}")
    changedPass = input("Enter the new password: ") # new password.
    with open('Password.txt', 'w') as f: # opens the Password.txt file in write mode.
        f.write(changedPass) # writes the changed password into the file
        print(f"Successfully changed password. The new password is {changedPass}") # sends a success print statement.


functionsList = [cardWriter, cardEditor, changePass, cardReader, classCard] # list of functions.

while True: # used to cause the program to not completely terminate.
    if Admin == True: # if the user is an admin.
        print("---------------------------------------------------------------------\n" # prints all the functions, including administrative ones.
        "press 1 if you want to write to a new file\n"
        "press 2 if you want to append the marks of an existing file\n"
        "press 3 if you want to change the password\n"
        "press 4 if you want to read the report card of a specific student\n"
        "press 5 if you want the class report\n"
        "press 0 if you want to exit\n")

        choice = int(input("Please input your choice: ")) # asks for the choice
        if choice in range(1, 6):
            print("-----------------------------------------------------------------")
            functionsList[choice-1]() # calls the function for the choice that is chosen.
        elif choice == 0: # if the choice is 0, it will terminate the program.
            print("now exiting the program\n"
                "-----------------------------------------------------------------")
            break
        else: # if the choice is neither of the above
            print("please enter a valid input thats listed below") # this error message is printed.
            continue
    elif Admin == False: # if the password is incorrect.
        print("---------------------------------------------------------------------\n" # prints all the non-administrative functions
            "press 1 if you want to read the report card of a student.\n" # like reading the report card of other students
            "press 2 if you want to read the class report card\n" # and reading the class card.
            "press 0 if you want to exit\n")
        choice = int(input("Please enter your choice.")) # asks for the choice.
        if choice in range(1,3): # if the choice is 1 or 2
            print("-----------------------------------------------------------------")
            functionsList[choice+2]() # choice + 1 is used to make sure that the user doesn't accidentally open a different function.
        elif choice == 0: # if the choice is 0
            print("Exiting")
            print("-----------------------------------------------------------------")
            break # the code is terminated.
        else: # if neither
            print("Enter a valid input") # prints this error message.
            continue
    else: # if the user is not an admin
        while True: # while true to keep it running.
            Passcheck = input("Please enter the administrative password: ") # asks for the predetermined password ('DPSI TEACHER PASS' by default.)
            if Passcheck == Password: # if the passcheck variable is the same as the admin password.
                print("Okay, confirmed.\nWelcome Admin.") # prints this statement
                Admin = True # sets admin to true
                break # breaks the code
            else: # if they get the password wrong.
                # this system will be revamped later on to make sure that you only get 3 extra attempts to get the password correct, otherwise the code will terminate.
                check = input("Are you sure you're an administrator? (Y/N)") # used to make sure that the user didn't input the incorrect password on accident.
                if check.lower() == 'y' or check.lower() == 'yes': # if it is yes
                    print("Okay, reloading.")
                    continue # reloads the password entering screen.
                elif check.lower() == 'n' or check.lower() == 'no': # if it is no
                    print("Okay, no problem.")
                    Admin = False # sets admin to false
                    break # and breaks the while loop to continue with non admin version of the code.
                else: # if neither
                    print("Invalid Input.") # error message
                    continue # prompt is re-asked
