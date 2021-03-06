def bubbleSort(inputList, desc = False):
    if not desc:
        for i in range(len(inputList)):
            for j in range(len(inputList) - i - 1):
                #this double for-loop lets each individual item in the list compare itself through the entire list                
                if inputList[j] > inputList[j + 1]:
                    temp = inputList[j]
                    inputList[j] = inputList[j + 1]
                    inputList[j + 1] = temp
            
    return inputList
            
    
                    
