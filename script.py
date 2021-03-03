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


currentMin = getMin(initialList)
currentMax = getMax(initialList)
counter = 0

while counter < len(initialList):
    for i in initialList:
        if i == currentMin:
            output.append(i)
            counter += 1
    currentMin += 1

print("The sorted list, from smallest to greatest: %s"%output)

            
        

        

