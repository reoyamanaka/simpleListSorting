from helperFunctions import getMin

def selectionSort(elements):
    size = len(elements)
    for i in range(size-1):
        minIndex = i
        for j in range(minIndex + 1, size):
            if elements[j] < elements[minIndex]:
                minIndex = j
        if i != minIndex:
            elements[i], elements[minIndex] = elements[minIndex], elements[i]

a = [1, 3, 4, 6, 2, 65]
selectionSort(a)
print(a)
