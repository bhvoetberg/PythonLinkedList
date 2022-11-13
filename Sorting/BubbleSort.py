def print_list(num_list):
    print(num_list)


def bubble_sort(original_list):
    length = len(original_list)
    for i in range (length -1, 0, -1):
        for index in range (i):
            if original_list[index] > original_list[index+1]:
                original_list[index+1], original_list[index] = \
                    original_list[index], original_list[index+ 1]
            print(' Unsorted till index: ', i - 1)
            print_list(original_list)

num_list = [10, 11, 5, 7, 2, 8, 3, 9, 6, 1, 4]

bubble_sort(num_list)
