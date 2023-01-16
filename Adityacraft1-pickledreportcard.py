import pickle

try:
    with open("class card", "rb") as classCard:
        file = pickle.load(classCard)
except: file = []

def find(arr: list, val):
    for i in arr:
        if val in i: return arr.index(i)
def valueCheckedInput(dtype=str, inputMessage="", r1=-100000000000, r2=100000000000, cLimit=10000):
    dtypeList = [str, int, float, bool]
    count = 0
    while count < cLimit:
        if dtype in dtypeList:
            try:
                x = dtype(input(f"{inputMessage}"))
                if x >= r1 and x <= r2:
                    return x
                else:
                    print(f"value must be between {r1} and {r2}")
                    continue
            except:
                count+=1
                print(f"value must be a {str(dtype)}")
                continue
        else:
            return 0
def nameCheck(val: str):
    strings = val.split()
    checkList = [i.isalpha() for i in strings]
    count = len([val for val in checkList if val == False])
    if count == 0: return True
    else: return False
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
    while True:
        name = input("Enter the student's name: ")
        if nameCheck(name) == True: break
        else: continue
    math_grade = valueCheckedInput(float, "Enter grade for Mathematics: ", 0, 100)
    computer_grade = valueCheckedInput(float, "Enter grade for Computer Science: ", 0, 100)
    english_grade = valueCheckedInput(float, "Enter grade for English: ", 0, 100)

    total_marks = math_grade + computer_grade + english_grade
    average_marks = total_marks / 3
    grade = grades(average_marks)
    report_card = [f"---------------------",
                  f"{name}'s report card:",
                  f"maths marks: {math_grade}",
                  f"computer marks: {computer_grade}",
                  f"english marks: {english_grade}",
                  f"Total marks: {total_marks}",
                  f"Average marks: {average_marks:.2f}",
                  f"Grade: {grade}"]
    file.append(report_card)
    with open("class card", 'wb') as classCard:
        pickle.dump(file, classCard)
def cardReader():
    name = input("Enter the student's name of whose report card you want: ")
    try:
        index = find(file, f"{name}'s report card:")
        reportCard = file[index]
        for i in reportCard:
            print(i)
    except:
        print("student was not found. please check spelling and capitalization")
def cardEditor():
    name = input("please enter the student's name who's card you wish to edit: ")
    try: index = find(file, f"{name}'s report card:")
    except: print("student was not found. please check spelling and capitalization"); return 0
    while True:
        subject = input(
            "please enter which subject's marks you wish to change (maths for maths, computer for computer science and english for english.): ")
        if subject.lower() == "maths":
            num = valueCheckedInput(float, 'Please enter the marks you want to change it to: ', 0, 100)
            file[index][3] = f'maths marks: {num}\n'
            break
        elif subject.lower() == "computer":
            num = valueCheckedInput(float, 'Please enter the marks you want to change it to: ', 0, 100)
            file[index][4] = f'computer marks: {num}\n'
            break
        elif subject.lower() == "english":
            num = valueCheckedInput(float, 'Please enter the marks you want to change it to: ', 0, 100)
            file[index][5] = f'english marks: {num}\n'
            break
        else:
            print("invalid value")
            continue
    with open("class card", 'wb') as classCard:
        pickle.dump(file, classCard)

functionsList = [cardWriter, cardReader, cardEditor]
while True:
    print("---------------------------------------------------------------------\n"
            "press 1 if you want to write to a new file\n"
            "press 2 if you want to read the report card of a specific student\n"
            "press 3 if you want to append the marks of an existing file\n"
            "press 0 if you want to exit\n")

    choice = valueCheckedInput(int, "please enter your choice: ", 0, 3)
    if choice in range(1, 4):
        print("-----------------------------------------------------------------")
        functionsList[choice - 1]()
    else:
        print("now exiting the program\n"
            "-----------------------------------------------------------------")
        break
