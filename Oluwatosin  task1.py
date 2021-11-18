# design task 1 by Tosin

reg_numbers = ["1256", "9876", "2378", "2199", "3301"]
student = {}
position = {}

for i in reg_numbers:
    record = [int(x) for x in input("enter quiz1, midterm, quiz2, and exams \n").split()]
    student[i] = dict(
        quiz1=record[0],
        midterm=record[1],
        quiz2=record[2],
        exams=record[3],
        total=sum(record),
    )

# print (student)


def getPosition():
    for k, v in student.items():
        position[k] = v["total"]
    newTuple = sorted(position.items(), key=lambda x: x[1], reverse=True)
    average = 0
    for i in range(len(newTuple)):
        average += newTuple[i][1] / len(newTuple)
        print(f"{newTuple[i][0]} with total {newTuple[i][1]} = {i+1} ")

    print(f"class highest {newTuple[0][0]} with total of {newTuple[0][1]}")
    print(f"class lowest {newTuple[4][0]} with total of {newTuple[4][1]}")
    print(f"class average {average}")



check = True
while check:
    print(
        "enter 1 to display record\nenter 2 to get positions ,summary and enter q to quit"
    )
    inppt = input()

    if inppt == "1":
        for k, v in student.items():
            print(
                f'student with regNumber {k} \t quiz1 :{v["quiz1"]} midterm:{v["midterm"]} quiz2:{v["quiz2"]} exams:{v["exams"]} total:{v["total"]}'
            )
    if inppt == "2":
        getPosition()

    if inppt.lower() == "q":
        check = False
