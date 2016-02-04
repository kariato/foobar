def answer(number):
    while len(str(number)) > 1:
        newNumber = 0
        for digit  in list(str(number)):
            newNumber += int(digit)
        number = newNumber
    return number
