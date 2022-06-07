ele = int(input("Enter the units: "))

def electricityCalculate(units):

    if (units <= 100):
        return units * 0
    elif (units <= 200):
        return  units * 4
    elif (units >= 201 & units <= 250):
        return units * 5
    elif (units >= 251 & units <= 300):
        return units * 8
    elif units > 301:
        return units * 15




print(electricityCalculate(ele))