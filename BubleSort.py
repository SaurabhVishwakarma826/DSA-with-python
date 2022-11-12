def BubleSort(elements):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped =True
        if not swapped:
            break


if __name__ == '__main__':
    elements = [1000,400,200,800]
    # elements = ["Saurabh","Rohit","Vishal","Khushboo"]
    sort = BubleSort(elements)
    print(elements)
