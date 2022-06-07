# 6. Tables

print("1. addition\n2. substraction\n3. Multiplication\n4. Division\n");

ope = int(input("Select the Operation: "))
tbno = int(input("Enter the table no: "))
tbino = int(input("Enter the table iteration: "))

def addition(tbn, tbi):
    for i in range(1, tbi):
        print(i," + ", tbn," = ", i + tbn)


def substraction(tbn, tbi):
    for i in range(1, tbi):
        print(i," - ",tbn," = ", i + tbn)

def multiplication(tbn, tbi):
    for i in range(1, tbi):
        print(i," * ",tbn," = ", i * tbn)

def division(tbn, tbi):
    for i  in range(1, tbi):
        print(i," / ",tbn," = ", i / tbn)


if ope == 1:
    addition(tbno, tbino)

if ope == 2:
    substraction(tbno,tbino)

if ope == 3:
    multiplication(tbno, tbino)

if ope == 4:
    division(tbno, tbino)



