def get_report_card():
    student_name = input("Enter the student's name of whose report card you want: ")
    student_name = student_name.capitalize()  # capitalize the name
    file_name = f"{student_name}.txt"

    try:
        with open(file_name, "r") as f:
            report_card = f.read()
        print(report_card)
    except FileNotFoundError:
        print(f"Report card for {student_name} not found.")

while True:
    names = []
    while not names:
        try:
            names = [str(x) for x in input("names (comma separated): ").split(", ")]
        except:
            print("invalid input")

    for i in names:
        i = i.capitalize()
        file = open(f"{i}.txt", "w")
        marks_input_valid = False
        while not marks_input_valid:
            try:
                mathsMarks = float(input(f"please input maths marks for {i}: "))
                csMarks = float(input(f"please input computer science marks for {i}: "))
                englishMarks = float(input(f"please input english marks for {i}: "))

                if mathsMarks in range(0, 101) and csMarks in range(0, 101) and englishMarks in range(0, 101):
                    marks_input_valid = True
                    avgMarks = ((mathsMarks + csMarks + englishMarks) / 3)
                    marksDict = {
                        range(90, 101): "A",
                        range(80, 90): "B",
                        range(70, 80): "C",
                        range(60, 70): "D",
                        range(0,50): "F"
                    }
                    grade = "F"  # default grade
                    for key in marksDict:
                        grade = marksDict[key]  # update grade
                        if round(avgMarks) in key:
                            break

                else:
                    print(" ")
                    print("The number has to be above 0 and below 100")
            except ValueError:
                print("invalid input")

        file.write("DELHI PUBLIC SCHOOL\n")
        file.write("-------------------\n")
        file.write(f"maths marks for {i}: {mathsMarks}\n")
        file.write(f"CS marks for {i}: {csMarks}\n")
        file.write(f"english marks for {i}: {englishMarks}\n")
        file.write(f"average marks: {round(avgMarks, 2)}\n")
        file.write(f"grade: {grade}\n")  # added newline character
        file.close()

    while True:
        get_report_card()  # fetch report card

        choice = input("Would you like to fetch another report card? (Y/N): ")
        if choice.lower() == "y":
            continue
        elif choice.lower() == "n":
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'")
    choice = input("Would you like to continue? (Y/N): ")
    if choice.lower() == "n":
        print("ending code")
        break
