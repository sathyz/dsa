"""Merge sort."""


def combine(left, right):
    arr = []
    n = len(left)
    m = len(right)
    i = 0
    j = 0

    while (i < n and j < m):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    # process left over items.
    for item in left[i:]:
        arr.append(item)

    for item in right[j:]:
        arr.append(item)
    # print(arr)
    return arr


def split(items):
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    # print(left, right)
    return left, right


def sort(items):
    if len(items) <= 1:
        result = items
    else:
        left, right = split(items)
        left_sorted = sort(left)
        right_sorted = sort(right)
        result = combine(left_sorted, right_sorted)
    return result


if __name__ == '__main__':
    items = [10, 3, 9, 5, 1, 2]
    print(items)
    print(sort(items))
