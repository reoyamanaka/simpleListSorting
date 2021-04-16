from random import shuffle
from helperFunctions import getMin, getMax
from bubbleSort import bubbleSort
from insertionSort import insertionSort

initialList = [x for x in range(10)]
shuffle(initialList)

def reshuffleAndShow(inputList):
    print("\nRe-randomizing list...")
    shuffle(inputList)
    print(inputList)
    print()

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

followUp = True
while followUp:
    print("\nLet's try another method for sorting. Choose from the list below:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    sortType = input()
    if sortType == "1":
        reshuffleAndShow(initialList)
        while True:
            print("Choose how you want to sort:")
            print("1. Ascending")
            print("2. Descending")
            sortDirection = input()
            if sortDirection == "1":
                print(bubbleSort(initialList))
                followUp = False
                break
            elif sortDirection == "2":
                followUp = False
                print(bubbleSort(initialList, desc=True))
                break
            else:
                print("\nInvalid entry. Choose either 1 or 2.\n")
    elif sortType == "2":
        reshuffleAndShow(initialList)
        while True:
            print("Choose how you want to sort:")
            print("1. Ascending")
            print("2. Descending")
            sortDirection = input()
            if sortDirection == "1":
                print(insertionSort(initialList))
                followUp = False
                break
            elif sortDirection == "2":
                print(insertionSort(initialList, desc = True))
                followUp = False
                break
    elif sortType == "3":
        reshuffleAndShow(initialList)
        while True:
            print("Choose how you want to sort:")
            print("1. Ascending")
            print("2. Descending")
            sortDirection=input()
            if sortDirection == "1":

    else:
        print("\nInvalid entry. Choose either 1 or 2.\n")
            
    
    
    
    

        
    

            
        

        

