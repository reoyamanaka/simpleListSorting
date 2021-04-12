def bubbleSort(inputList, desc = False):
    for i in range(len(inputList)):
        for j in range(len(inputList) - i - 1):
            if not desc:
                #this double for-loop lets each individual item in the list compare itself through the entire list                
                if inputList[j] > inputList[j + 1]:
                    temp = inputList[j]
                    inputList[j] = inputList[j + 1]
                    inputList[j + 1] = temp
            else:
                if inputList[j] < inputList[j + 1]:
                    temp = inputList[j]
                    inputList[j] = inputList[j + 1]
                    inputList[j + 1] = temp
    return inputList
            
    
                    
