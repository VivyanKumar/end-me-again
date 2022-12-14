while True:
    try:
        choice = input("would you like to continue?(Y/N): ")
        if choice.lower() == "y":
            print("continuing")
        elif choice.lower() == "n":
            print("ending code")
            print("updating files")
            break
        else:
            print("invalid input")
            continue
    except:
        print("invalid input")
        
    try:
        names = [str(x) for x in input("names: ").split(", ")]
    except:
        print("invalid input")

    for i in names:
        i = i.capitalize()
        file = open(f"{i}.txt", "w")
        mathsMarks = float(input(f"please input maths marks for {i}: "))
        csMarks = float(input(f"please input computer science marks for {i}: "))
        englishMarks = float(input(f"please input english marks for {i}: "))

        if mathsMarks in range(0, 101) and csMarks in range(0, 101) and englishMarks in range(0, 101):
            global avgMarks
            avgMarks = ((mathsMarks + csMarks + englishMarks) / 3)
            marksDict = {
                range(90, 101): "A",
                range(80, 90): "B",
                range(70, 80): "C",
                range(60, 70): "D",
            }
            if avgMarks in marksDict:
                grade = marksDict[avgMarks]
            else:
                grade = "Fail"
        else:
            print(" ")
            print("The number has to be above 0 and below 100")

        file.write("DELHI PUBLIC SCHOOL\n")
        file.write("-------------------\n")
        file.write(f"maths marks for {i}: {mathsMarks}\n")
        file.write(f"CS marks for {i}: {csMarks}\n")
        file.write(f"english marks for {i}: {englishMarks}\n")
        file.write(f"average marks: {round(avgMarks, 2)}\n")
        file.write(f"grade: {grade}")
        file.close()
