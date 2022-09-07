def bin_search(array, n, i=0):

    if n == array[0]:
        return i
    elif n != array[0] and len(array) == 1:
        return -1
    mid = len(array) // 2

    if n >= array[mid]:
        return bin_search(array[mid:], n, i + mid)
    else:
        return bin_search(array[:mid], n, i)


print('Index: ' + str(bin_search(range(10, 1000), 14)))
