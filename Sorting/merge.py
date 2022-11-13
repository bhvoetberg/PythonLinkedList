def print_list(num_list):
    print(num_list)


def merge_sort(original_list):
    if len(original_list) <= 1:
        return

    mid = len(original_list) // 2

    lefthalf = original_list[:mid]
    righthalf = original_list[mid:]

    merge_sort(lefthalf)
    print_list(lefthalf)

    merge_sort(righthalf)
    print_list(righthalf)

    # index for lefthalf sublist
    i = 0
    # index for righthald sublist
    j = 0
    # index for original list
    k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            original_list[k] = lefthalf[i]

            i + i + 1
        else:
            original_list[k] = righthalf[j]
            j = j + 1
        k = k + 1

        while i < len(lefthalf):
            original_list[k] = lefthalf[i]

            i = i + 1
            k = k + 1

            while j < len(righthalf):
                original_list[k] = righthalf[j]

            j = j + 1
            k = k + 1


num_list = [10, 11, 5, 7, 2, 8, 3, 9, 6, 1, 4]

merge_sort(num_list)
