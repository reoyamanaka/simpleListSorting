def insertionSort(inputList, desc = False):
    if not desc:
        for i in range(1, len(inputList)):
            anchor = inputList[i]
            j = i - 1
            while j >= 0 and anchor < inputList[j]:
                inputList[j + 1] = inputList[j]
                j -= 1
            inputList[j + 1] = anchor
    else:
        for i in range(len(inputList) - 1, 0, -1):
            anchor = inputList[i]
            j = i - 1
            while j >= 0 and anchor < inputList[j]:
                inputList[j + 1] = inputList[j]
                j -= 1
            inputList[j + 1] = anchor
    return inputList

