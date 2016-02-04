define answer(number):
    pads = 0
    while number > 0:
        number -= int(math.pow(int(math.sqrt(number)),2))
        pads +=1
    return pads
