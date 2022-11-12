
# def BubleSort(elements, key):
#     size = len(key)
#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1):
#             if elements[j][key] > elements[j+1][key]:
#                 temp = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1] = temp
#                 swapped =True
#         if not swapped:
#             break
#
#
#
# if __name__ == '__main__':
#     elements = [
#         {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
#         {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
#         {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
#         {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]
#     BubleSort(elements, key='transaction_amount')
#     print(elements)


def BubleSort(elements):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1):
            if elements[j][1] > elements[j+1][1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped =True
        if not swapped:
            break


s = [[1,3],[3,1],[5,4],[4,0]]
BubleSort(s)
print(s)