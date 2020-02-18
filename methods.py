def sort_countion(array):
    another_array = array.copy()
    for i in range(len(array)):
        less = 0
        for o in range(len(array)):
            if array[i] > array[o]:
                less += 1
            elif array[i] == array[o] and i > o:
                less += 1
        another_array[less] = array[i]
    return another_array


def sort_include(array):
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            for o in range(i):
                if array[o] > array[i + 1]:
                    for p in range(o, i):
                        array[p] = array[p - 1]
                    array[o] = array[i + 1]
                    break
    return array


def sort_shell(array):
    t = int(len(array) / 2)
    while t > 0:
        for i in range(len(array) - t):
            j = i
            while j >= 0 and array[j] > array[j + t]:
                array[j], array[j + t] = array[j + t], array[j]
                j -= 1
        t = int(t / 2)
    return array


def sort_eject(array):
    for i in range(len(array)):
        num = i
        for o in range(i, len(array)):
            if array[o] < array[num]:
                num = o
        array[i], array[num] = array[num], array[i]
    return array


def sort_tree(array):
    n = len(array)
    for i in range(n, -1, -1):
        tree(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        tree(array, i, 0)
    return array


def tree(array, size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < size and array[left_child] > array[largest]:
        largest = left_child
    if right_child < size and array[right_child] > array[largest]:
        largest = right_child
    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        tree(array, size, largest)


def sort_bubble(array):
    for i in range(len(array)):
        o = i
        while o != 0 and array[o] < array[o - 1]:
            array[o - 1], array[o] = array[o], array[o - 1]
            o -= 1
    return array


def sort_quick_sort(array):
    pass


def sort_merge(array):
    mid = len(array) // 2
    left_list = sort_merge(array[:mid])
    right_list = sort_merge(array[mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def sort_distribution(array):
    pass
