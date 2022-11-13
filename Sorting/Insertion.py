def print_list(num_list):
    print(num_list)


def insertion_sort(original_list):
    length = len(original_list)
    for i in range (0, length -1):
        for j in range (i+1, 0, -1):
            if original_list[j] < original_list[j-1]:
                original_list[j], original_list[j-1] = \
                    original_list[j-1], original_list[j]
            print(' Unsorted till index: ', i)
            print_list(original_list)

num_list = [10, 11, 5, 7, 2, 8, 3, 9, 6, 1, 4]

insertion_sort(num_list)