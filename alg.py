import random

def binary_search(goal, it):
    return _binary_search(goal, it, 0, len(it)-1)

def _binary_search(goal, m, first, last):
    mid = (first + last) // 2
    if m[mid] == goal:
        return (True, mid)
    if first >= last:
        return (False, None)
    if m[mid] > goal:
        return _binary_search(goal, m, first, mid-1)
    else:
        return _binary_search(goal, m, mid+1, last)


