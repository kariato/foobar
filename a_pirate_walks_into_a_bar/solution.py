def answer(numbers):
    pirates = [0]
    for pirate in numbers:
        if pirate in pirates:
            return len(pirates) - pirates.index(pirate)
        pirates.append(pirate)
