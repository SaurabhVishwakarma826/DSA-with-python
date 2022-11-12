def InsertionSort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j-=1
        elements[j+1] = anchor  

if __name__ == '__main__':
    elements = [4,2,5,5,7,2,4,753,5,3]
    InsertionSort(elements)
    print(elements)