# Sorted list required

def binary_search(sorted_list, key):
    min_index = 0
    max_index = len(sorted_list) - 1

    while (min_index <= max_index):
        mid = (min_index + max_index) //2
        if sorted_list[mid] == key:
            return mid
        elif sorted_list[mid] < key:
            min_index = mid + 1
        else:
            max_index = mid - 1

    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(binary_search(list, 9))
