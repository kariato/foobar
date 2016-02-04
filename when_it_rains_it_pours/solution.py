"""
The solution to the "when_it_rains_it_pours" problem.
"""

def answer(numbers):
    waterLevel = 0
    numbers2=[0]*len(numbers)
    for loop in range(1,len(numbers)-1):
        numbers2[loop] = min(max(numbers[:loop]),max(numbers[loop:]))
    for loop in range(1,len(numbers)-1):
        if numbers2[loop] > numbers[loop]:
            waterLevel += numbers2[loop] - numbers[loop]
    return waterLevel
