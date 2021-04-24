def selectionSort(elements, desc = False):
    if not desc:
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

    return elements
