def shel_sort(elements):
    ele = list(set(elements))
    size = len(ele)
    gap = size//2
    while gap > 0:
        for i in range(gap, size):
            anchor = ele[i]
            j = i
            while j>=gap and ele[j-gap] > anchor:
                ele[j] = ele[j-gap]
                j -= gap
            ele[j] = anchor
        gap = gap//2
    print(ele)

if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 2, 5, 8, 3]
    shel_sort(elements)
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]
    for i in tests:
        shel_sort(i)
        # print(i)

