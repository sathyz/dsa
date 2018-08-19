def search(arr, item):
    # print("search {} in {}".format(item, arr))
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        # print("arr[{}] = {}".format(mid, arr[mid]))
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1
        else:
            return mid
        # print("search({}, {})".format(low, high))
    else:
        return low - 1


if __name__ == '__main__':
    arr = [2, 5, 10, 20, 50, 90, 100]
    # print("test 1")
    # for item in arr:
    #     print(search(arr, item))
    #
    for item in [1, 2, 3, 5, 6, 95, 100, 105]:
        index = search(arr, item)
        print("Found {} at {}".format(item, index))

    # print("test 3")
    # for item in arr:
    #     print(search(arr, item - 1))
