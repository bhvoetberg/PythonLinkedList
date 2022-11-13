def print_list(num_list):
    print(num_list)


def shell_sort(original_list):
    length = len(original_list)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            temp = original_list[i]
            j = i

            while j >= gap and original_list[j - gap] > temp:
                original_list[j] = original_list[j - gap]
                j -= gap

            original_list[j] = temp

            print(' Gap: ', gap)
            print_list(original_list)
        gap = gap // 2


num_list = [10, 11, 5, 7, 2, 8, 3, 9, 6, 1, 4]

shell_sort(num_list)
