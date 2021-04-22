def selectionSort(elements, reverse = False):
    if not reverse:
        for i in range(len(elements) - 1):
            minIndex = i
            for j in range(minIndex + 1, len(elements)):
                if elements[j] < elements[minIndex]:
                    minIndex = j
            if i != minIndex:
                temp = elements[i]
                elements[i] = elements[minIndex]
                elements[minIndex] = temp

    else:
        for i in range(len(elements) - 1):
            minIndex = i
            for j in range(minIndex + 1, len(elements)):
                if elements[j] > elements[minIndex]:
                    minIndex = j
            if i != minIndex:
                temp = elements[i]
                elements[i] = elements[minIndex]
                elements[minIndex] = temp

from random import shuffle
a = []
for i in range(10):
    a.append(i)

shuffle(a)
print(a)
selectionSort(a)
print(a)
selectionSort(a, reverse = True)
print(a)


