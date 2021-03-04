from random import shuffle
from helperFunctions import getMin, getMax
initialList = [x for x in range(10)]
shuffle(initialList)

print("Initial randomized list: %s"%initialList)
output = []

while True:
    print("How do you want to sort the randomized list?")
    print("1. Increasing")
    print("2. Decreasing")
    sortingOption = input()
    currentMin = getMin(initialList)
    currentMax = getMax(initialList)
    counter = 0
    if sortingOption == "1":
        while counter < len(initialList):
            for i in initialList:
                if i == currentMin:
                    output.append(i)
                    counter += 1
            currentMin += 1
        print("The sorted list, from smallest to greatest: %s"%output)
        break
    elif sortingOption == "2":
        while counter < len(initialList):
            for i in initialList:
                if i == currentMax:
                    output.append(i)
                    counter += 1
            currentMax -= 1
        print("The sorted list, from greatest to smallest: %s"%output)
        break
    else:
        print("\nInvalid entry. Choose either 1 or 2.\n")

        
    

            
        

        

