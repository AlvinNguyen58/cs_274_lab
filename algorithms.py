"""Implementations of some sorting"""
import random
import ArrayList


def linear_search(a: ArrayList.ArrayList, x):
    # todo
    for i in range(a.size()):
        if x == a[i]:
            return i
    return -100
    pass


def binary_search(a: ArrayList.ArrayList, x):
    # todo
    l = 0
    r = a.size() - 1
    while l <= r:
        m = 1 + r // 2
        if a[m] == x:
            return x
        elif x < a[m]:
            r = m - 1
        else:
            l = m + 1
    return -100
    pass


def _merge(a0: ArrayList.ArrayList, a1: ArrayList.ArrayList, a: ArrayList.ArrayList):
    # todo
    i0 = 0
    i1 = 0
    for i in range(a.size() - 1):
        if i0 == a.size():
            a[i] = a1[i1]
            i1 = 1
        elif i == a.size():
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
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
    m = n // 2
    a0 = a[0: m - 1]
    a1 = a[m: a.size() - 1]
    merge_sort(a0)
    merge_sort(a1)
    merge(a0, a1, a)
    pass


def _quick_sort_f(a: ArrayList.ArrayList, start, end):
    # todo
    pass


def _quick_sort_r(a: ArrayList.ArrayList, start, end):
    # todo
    pass


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
