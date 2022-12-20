ListMarks = [] # Used later in the code to calculate class average (12:30 am mush brain could only think of this)
def get_report_card(): # function used to send the report card of the student into the console.
    student_name = input("Enter the student's name of whose report card you want, or, input class for the class average: ")
    if student_name.lower() != 'class': # checks if the user wants the class average or not.
        student_name = student_name.capitalize()  # capitalize the name
        file_name = f"{student_name}.txt" # the file name
        try:
            with open(file_name, "r") as f: # making it easier to work with.
                report_card = f.read() # reads the report card and stores it into a variable
            print(report_card) # prints the report card
        except FileNotFoundError: # If there is a FileNotFoundError
            print(f"Report card for {student_name} not found.") # This is printed.
    else: # If the input is class
        print(f'The class average is {ClassAverage}') # prints the class average
while True: # Used to keep the code in a continous loop
    names = []
    while not names: # no clue
        try:
            names = [str(x) for x in input("Enter the names of the students, seperating with a comma and a space. (Example: Ihit, Vivyan, Aarav Saini, Aditya G Das): ").split(", ")] # Asks for names
        except:
            print("invalid input")

    for i in names: # loops mainly for creating files
        i = i.capitalize() # Capitalizes the first letter to make it look better (I think)
        file = open(f"{i}.txt", "w") # Opens a file with the name of the student
        marks_input_valid = False # Checks if the marks input are valid (Thanks to Rathiin for this)
        while not marks_input_valid: # While not False.
            try:
                # Float inputs for maths, computer science and english percentage.
                mathsMarks = float(input(f"Please input the Maths percentange of  {i}: ")) 
                csMarks = float(input(f"Please input the Computer Science percentage of {i}: "))
                englishMarks = float(input(f"Please input the English percentage of {i}: "))

                if round(mathsMarks) in range(0, 101) and round(csMarks) in range(0, 101) and round(englishMarks) in range(0, 101): # Checks if the numbers input are in the range 0-100
                    marks_input_valid = True # Sets the validity check to True
                    avgMarks = ((mathsMarks + csMarks + englishMarks) / 3) # Takes out the average marks of the student
                    ListMarks.append(avgMarks) # Appends these average marks into a list to be used later.
                    marksDict = { # Dictionary is used to make the code cleaner, instead of using if and elif statements over and over again.
                        range(90, 101): "A",
                        range(80, 90): "B",
                        range(70, 80): "C",
                        range(60, 70): "D",
                        range(0, 60): 'Fail'
                    }
                    for key in marksDict: # Used to check if the average marks are in the grade thresholds
                        global grade
                        grade = marksDict[key]  # Updates the grades
                        if round(avgMarks) in key: # Checks if the integer value of average marks is in the threshold.
                            break
                    
                else:
                    print(" ")
                    print("The number has to be above 0 and below 100") # Error message for the checking of marks in range 0-100
            except ValueError: # If a value error occurs, the print statement is sent.
                print("Invalid input") 
        # Writing in the file opened at the beginning of the program.
        file.write("-------------------\n")
        file.write("DELHI PUBLIC SCHOOL\n")
        file.write("-------------------\n")
        file.write(f"maths marks for {i}: {mathsMarks}\n")
        file.write(f"CS marks for {i}: {csMarks}\n")
        file.write(f"english marks for {i}: {englishMarks}\n")
        file.write(f"average marks: {round(avgMarks, 2)}\n")
        file.write(f"grade: {grade}\n")  # added newline character
        file.close()
    # The Class Average Calculator.
    ClassAverage = 0
    ClassAverage = round(sum(ListMarks) / len(names))
    with open("ClassAverage.txt", "w") as f: # Opens ClassAverage.txt, write only mode as f.
        f.write(f'The average of the class is: {ClassAverage}') # Writes this single line into the file
        f.close() # Closes the file
    while True:
        get_report_card()  # Fetches report card

        choice = input("Would you like to fetch another report card? (Y/N): ") # Checks if the user wants to get another report card
        if choice.lower() == "y" or choice.lower() == 'yes':
            continue
        elif choice.lower() == "n" or choice.lower() == 'no':
            break
        else: 
            print("Invalid input. Please enter 'Y' or 'N'")
    choice = input("Would you like to continue? (Y/N): ") # Continuation Prompt.
    if choice.lower() == "n" or choice.lower() == 'no':
        print("Okay! Updating files...") # Fancy lingo for saving files
        print("Done! Terminating Program...") # Fancy lingo for shutting off the program
        break # Breaks the original while loop.
