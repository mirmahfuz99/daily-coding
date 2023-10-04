
def binarySearch(list,n):

    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            pos = mid
            return pos + 1
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return -1                    

print(binarySearch([1,2,3,4,5,6,7,8], 9))