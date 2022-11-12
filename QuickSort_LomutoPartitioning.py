def swap(a,b,arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements, start, end):
    pivot = elements[end]
    pindex = start
    for i in range(start,end):
        if elements[i] <= pivot:
            swap(pindex,i,elements)
            pindex+=1
    swap(pindex,end, elements)
    return pindex

def QuickSort(elements, start ,end):
    if len(elements) == 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        QuickSort(elements, start, pi-1)
        QuickSort(elements, pi+1, end)



if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    QuickSort(elements,0, len(elements)-1)
    print(elements)
