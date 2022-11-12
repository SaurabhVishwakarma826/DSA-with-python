
########################   PROBLEM STATEMENT ############################
# Binary Search Exercise
# When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
#
# numbers = [1,4,6,9,10,5,7]

# def sorted_number(number_list):
#     sort = number_list
#     return sorted(sort)

def binar_search(numbers_list,number_to_find):
    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        mid_number = numbers_list[mid_index]
        if mid_number == number_to_find:
            return mid_index
        if number_to_find > mid_number:
            left_index = mid_index+1
        else:
            right_index = mid_index-1
    return -1

def find_all_occurences(number_list,number_to_find):
    index = binar_search(number_list,number_to_find)
    indecs = [index]
    i = index-1
    while i >= 0:
        if number_list[i] == number_to_find:
            indecs.append(i)
        else:
            break
        i = i -1

    i = index+1
    while i <= len(number_list):
        if number_list[i] == number_to_find:
            indecs.append(i)
        else:
            break
        i = i + 1
    return sorted(indecs)

if __name__ == '__main__':
    # numbers1 = [1, 4, 6, 9, 10, 5, 7]
    # find = binar_search(numbers1,5)
    # print(f"Number find at {find}")


    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    search = find_all_occurences(numbers,15)
    print(f"Number find at {search} ")