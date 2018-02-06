def get_valid_unit():
    while True:
        firstInput = input("Convert from unit: ")
        if firstInput == 'm':
            unit1= firstInput
            break
        elif firstInput == 'ft':
            unit1= firstInput
            break
        else:
            print(firstInput,"is not a valid unit\n")

    while True:
        secondInput = input("Convert to unit: ")
        if secondInput == 'm':
            unit2 = secondInput
            break
        elif secondInput == 'ft':
            unit2 = secondInput
            break
        else:
            print(secondInput,"is not a valid unit\n")

    units = (unit1,unit2)
    return units


def get_valid_number():
    while True:
        userInput = input("Length to convert\n")
        if userInput.isdigit():
            return int(userInput)
        else:
            print (userInput,"is not a valid integer\n")

def convert(number, from_unit, to_unit):
    if (from_unit=='m')&(to_unit=='ft'):
        print("Converted from m to ft:",number*3.281,to_unit)
    elif (from_unit=='ft')&(to_unit=='m'):
        print("Converted from ft to m:",number*0.305,to_unit)
    elif from_unit==to_unit:
        print("Same unit conversion:",number,to_unit)
    else:
        print("error")

def conversion():
    units=get_valid_unit()
    number=get_valid_number()
    convert(number,units[0],units[1])


if __name__ == '__main__':
    conversion()
