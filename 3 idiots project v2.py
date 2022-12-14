# To ensure that the code keeps running.
while True:
    # Try ensures that the user cannot cause an error.
    try:
        # choice is the input required.
        choice = input("Would you like to continue? (Y/N) : ")
        # if choice is yes, the code will continue.
        if choice.lower() == "y" or 'yes':
            print("Okay! Continuing... \n")
        # if the choice is no, the code will break and the files will be updated.
        if choice.lower() == "n" or 'no':
            print("Okay! Updating Files... \n")
            print("All done! Closing... \n")
            break
        # if the choice is neither yes nor no, an error message will be displayed.
        else:
            print("The answer must be yes or no")
            continue
    # Except condition for the Try condition
    except:
        print("Invalid Input.")
    # Try is used to get all the names of the students.
    try:
        names = [str(x) for x in input("Enter the names of the students here, seperating with a comma and space. (Example: Aditya, Rathiin, Ihit, Vivyan): ").split(", ")]
    # Except for the Try condition is used to make sure that the user has inputted the names correctly.
    except:
        print("Invalid Input. (Did you add a comma and space between the names?) ")
    # For loop used for inputting the percentages of the students, calculating their average marks, getting their grades, and inputting it all into a file.
    for i in names:
        # i = i.capitalize() is not required, it is just used for cosmetic purposes.
        i = i.capitalize()
        # Opens a file with the name of the student.
        file = open(f"{i}.txt", "w")
        # Checks if the input is a number and prevents an error.
        try:
            # Asks for the subject percentages of each student.
            mathsMarks = float(input(f"Please enter the Maths percentage of {i}: "))
            csMarks = float(input(f"Please enter the Computer Science percentage of {i}: "))
            englishMarks = float(input(f"Please enter the English percentage of {i}: "))
            # Checks if the input is in the acceptable range.
            if mathsMarks in range(0, 101) and csMarks in range(0, 101) and englishMarks in range(0, 101):
                # Declares avgMarks as a global variable to avoid undefined errors.
                global avgMarks
                # Calculates the average marks of each student.
                avgMarks = ((mathsMarks + csMarks + englishMarks) / 3)
                # Dictionary used to check for grade thresholds to prevent messy (if) statements.
                marksDict = {
                    range(90, 101): "A",
                    range(80, 90): "B",
                    range(70, 80): "C",
                    range(60, 70): "D",
                }
                # Checks if the grade thresholds apply to the average.
                if avgMarks in marksDict:
                    grade = marksDict[avgMarks]
                # If the average is not in the grade thresholds, the student has a failing grade.
                else:
                    grade = "Fail"
            # Error for incorrect input (if the number is not in the range.)
            else:
                print(" ")
                print("The number has to be above 0 and below 100")
                    # File writing.
            file.write("DELHI PUBLIC SCHOOL\n")
            file.write("-------------------\n")
            file.write(f"The maths percentage of {i} is: {mathsMarks}\n")
            file.write(f"The computer science percentage of {i} is: {csMarks}\n")
            file.write(f"The english percentage {i} is: {englishMarks}\n")
            file.write(f"The average of {i} is: {round(avgMarks, 2)}. This is a/an {grade}. \n")
            file.close()
        # Except for the try statement. Tells the user that the input is invalid.
        except:
            print("Invalid Input. The percentages must be a number.")
