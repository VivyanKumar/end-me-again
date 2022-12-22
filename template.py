import pyfiglet

print(pyfiglet.figlet_format("DPSI"))

def cardWriter():
    print("writing")
def cardReader():
    print("reading")
    student_name = input(
        "Enter the student's name of whose report card you want, or, input class for the class average: ")
    if student_name.lower() != 'class':  # checks if the user wants the class average or not.
        student_name = student_name.capitalize()  # capitalize the name
        file_name = f"{student_name}.txt"  # the file name
        try:
            with open(file_name, "r") as f:  # making it easier to work with.
                report_card = f.read()  # reads the report card and stores it into a variable
            print(report_card)  # prints the report card
        except FileNotFoundError:  # If there is a FileNotFoundError
            print(f"Report card for {student_name} not found.")  # This is printed.
    else:  # If the input is class
        print(f'The class average is {ClassAverage}')  # prints the class average
def cardEditor():
    print("editing")
def classCard():
    print("getting the card")

functionsList = [cardWriter, cardReader, cardEditor, classCard]

while True:
    print("---------------------------------------------------------------------\n"
          "press 1 if you want to write to a new file\n"
          "press 2 if you want to append the marks of an existing file\n"
          "press 3 if you want to read the report card of a specific student\n"
          "press 4 if you want the class report\n"
          "press 0 if you want to exit\n")

    try:
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
    except:
        print("please enter a valid input thats listed below")
        continue
