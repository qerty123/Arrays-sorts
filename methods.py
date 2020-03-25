from random import randint
from functools import reduce


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


def sort_quick(array):
    if len(array) <= 1:
        return array
    else:
        q = array[randint(0, len(array) - 1)]
    l_nums = [n for n in array if n < q]
    e_nums = [q] * array.count(q)
    b_nums = [n for n in array if n > q]
    return sort_quick(l_nums) + e_nums + sort_quick(b_nums)


def sort_merge(array):
    length = len(array)
    if length >= 2:
        mid = int(length / 2)
        array = merge(sort_merge(array[:mid]), sort_merge(array[mid:]))
    return array


def merge(left, right):
    array = []
    while left and right:
        if left[0] < right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))
    if left:
        array.extend(left)
    if right:
        array.extend(right)
    return array


def sort_bitwise(array):
    shift = 1
    for x in range(len_number(max(array))):
        result = [[] for _ in range(10)]
        numbers = [x for x in range(10)]
        for e, num in enumerate(numbers):
            for arr in array:
                if num == arr % (shift * 10) // shift:
                    result[e].append(arr)
        array = reduce(lambda x, y: x + y, result)
        shift = shift * 10
    return array


def len_number(num):
    c = 0
    while num:
        num //= 10
        c += 1
    return c
