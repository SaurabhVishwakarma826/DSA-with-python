def merg_sort(arr):
    if len(arr) <=1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merg_sort(left)
    merg_sort(right)
    merg_tow_sorted_arr(left,right,arr)

def merg_tow_sorted_arr(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i=j=k=0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i<len_a:
        arr[k] =  a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k] = b[j]
        j+=1
        k+=1

def remove(elements):
    merg_sort(elements)
    while len(elements) > 1:
        del(elements[0])
        if len(elements) > 1:
            del(elements[len(elements)-1])
    print(elements)


if __name__ == '__main__':
    elements = [7,8,3,4,2,9,5]
    remove(elements)


