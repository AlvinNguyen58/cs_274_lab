"""Implementations of some sorting"""
import random
import ArrayList


def linear_search(a: ArrayList.ArrayList, x):
    # todo
    for i in range(a.size()):
        if x is a[i]:
            return i
    return -100
    pass


def binary_search(a: ArrayList.ArrayList, x):
    # todo
    l = 0
    r = a.size() - 1
    while l <= r:
        m = l + r // 2
        if a[m] == x:
            return m
        elif x < a[m]:
            r = m - 1
        else:
            l = m + 1
        print(m)
    return -100


def _merge(a0: ArrayList.ArrayList, a1: ArrayList.ArrayList, a: ArrayList.ArrayList):
    # todo
    i0, i1 = 0, 0
    for i in range(a.size()):
        if i0 == a0.size():
            a[i] = a1[i1]
            i1 += 1
        elif i1 == a1.size():
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] < a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1
    pass


def merge_sort(a: ArrayList.ArrayList):
    # todo
    if a.size() <= 1:
        return
    m = a.size() // 2
    a0 = ArrayList.ArrayList()
    for i in range(0, m):
        a0.append(a[i])
    a1 = ArrayList.ArrayList()
    for i in range(m, a.size()):
        a1.append(a[i])
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)
    pass


def _quick_sort_f(a: ArrayList.ArrayList, start, end):
    # todo
    if start < end:
        p = _partition(a, start, end)
        _quick_sort_f(a, start, p - 1)
        _quick_sort_f(a, p + 1, end)
    pass


def _quick_sort_r(a: ArrayList.ArrayList, start, end):
    # todo
    if start < end:
        r = random.randint(start, end)
        a[r], a[start] = a[start], a[r]
        _quick_sort_f(a, start, end)


def _partition(a, start, end):
    pivot = a[start]
    l = start + 1
    r = end
    crossed = False
    while not crossed:
        while l <= r and a[l] <= pivot:
            l += 1
        while r >= l and a[r] >= pivot:
            r -= 1
        if r < l:
            crossed = True
        else:
            a[l], a[r] = a[r], a[l]
    a[start], a[r] = a[r], a[start]
    return r


def quick_sort(a: ArrayList.ArrayList, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)
