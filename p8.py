student_details = [
    ['21CSEA35','vishwanath',9876543227],
    ['21CSEA34','venkat',7896547896],
    ['21CSEA33','Tamil selvan',8764567897]
]

screen = int(input("1. View students details\n2. Add new student\n"))


if screen == 1:
    print("Regno         Name         Phone");
    for i in range(len(student_details)):
        print(student_details[i][0], " ", student_details[i][1], " ", student_details[i][2])

if screen == 2:
    # add new details
    regno = input("Enter the Regno: ")
    name = input("Enter the Name: ")
    phone = int(input("Enter the phone no: "))

    new_details = [regno, name, phone];
    student_details.append(new_details);
    print("Regno         Name         Phone");
    for i in range(len(student_details)):
        print(student_details[i][0], " ", student_details[i][1], " ", student_details[i][2])



