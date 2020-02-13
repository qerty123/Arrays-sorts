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
    pass


def sort_bubble(array):
    for i in range(len(array)):
        o = i
        while o != 0 and array[o] < array[o - 1]:
            array[o - 1], array[o] = array[o], array[o - 1]
            o -= 1
    return array


def sort_quick_sort(array):
    pass
