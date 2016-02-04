def answer(numbers):
    pirates = []
    lastPirate = 0
    while lastPirate not in pirates:
        pirates.append(lastPirate)
        lastPirate=numbers[lastPirate]
    return len(pirates) - pirates.index(lastPirate)

