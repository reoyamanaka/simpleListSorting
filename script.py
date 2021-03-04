from random import shuffle
initialList = [x for x in range(10)]
shuffle(initialList)

print("Initial randomized list: %s"%initialList)
output = []

def getMin(inputList):
    currentMin = inputList[0]
    for i in range(len(inputList)-1):
        if inputList[i + 1] < currentMin:
            currentMin = inputList[i + 1]
    return currentMin

def getMax(inputList):
    currentMax = inputList[0]
    for i in range(len(inputList) - 1):
        if inputList[i + 1] > currentMax:
            currentMax = inputList[i + 1]
    return currentMax


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
elif sortingOption == "2":
    while counter < len(initialList):
        for i in initialList:
            if i == currentMax:
                output.append(i)
                counter += 1
        currentMax -= 1
    print("The sorted list, from greatest to smallest: %s"%output)
    

            
        

        

