student_report_cards = {}  # dictionary to store the report cards of all students

while True:
    # Ask for the student's name
    name = input("Enter the student's name: ")

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

    # Calculate the total marks
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
    report_card = f"---------------------\n{name}'s report card:\nTotal marks: {total_marks}\nAverage marks: {average_marks:.2f}\nGrade: {grade}\n---------------------\n"

    # Save the report card for the student in the dictionary
    student_report_cards[name] = report_card

    # Save the report card to a file
    with open(f"{name} report card.txt", "w") as f:
        f.write(report_card)
    # Ask the user for which student's report card they want to view
    while True:
        student_name = input("Enter the name of the student whose report card you want to view: ")
        if student_name in student_report_cards:
            print(student_report_cards[student_name])
            break
        else:
            print("Student not found. Please enter a valid student name.")

    # Ask if the user wants to continue
    user_input = input("Do you want to continue? (y/n) ")
    if user_input == "n":
        break
    elif user_input != "y":
        print("Invalid input. Please enter 'y' or 'n'.")
