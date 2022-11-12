def selectionSort(arr):
    size = len(arr)
    for i in range(size-1):
        mid_index = i
        for j in range(mid_index+1,size):
            if arr[j]<arr[mid_index]:
                mid_index = j
        if i != mid_index:
            arr[i],arr[mid_index] = arr[mid_index],arr[i]

if __name__ == '__main__':
    arr = [3,2,4,5,0,1,7,4]
    selectionSort(arr)
    print(arr)
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for i in(tests):
        selectionSort(i)
        print(i)
