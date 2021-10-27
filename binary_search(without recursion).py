def binary_search(l, num):
    beg = 0
    last = len(l) - 1
    flag = 0
    while (beg <= last and flag == 0):
        mid = (beg + last) // 2
        if l[mid] == num:
            flag = 1
            elif l[mid] > num:
            last = mid - 1
    else:
        beg = mid + 1
    return flag

print(binary_search())
