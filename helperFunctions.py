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
