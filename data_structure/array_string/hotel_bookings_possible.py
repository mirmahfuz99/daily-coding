
def hotel(arrive, depart, k):
    arrive.sort()
    depart.sort()

    count = 0
    n = len(arrive)

    i, j = 0, 0

    while i < n and j < n:
        if arrive[i] < depart[j]:
            print("arrive",arrive[i])
            print("depart", depart[j])

            count += 1
            print("count:",count)
            if count > k:
                return False
            i += 1
        else:
            count -= 1
            print(count)
            j += 1
    return True

print(hotel([1,1,1], [1,1,4], 1)  )                  