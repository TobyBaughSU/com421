def sort(a: list):
    isSorted = False
    sortIndex = len(a)-1

    while not isSorted:
        isSorted = True
        tempSortIndex = None
        for i in range(sortIndex):
            if a[i] > a[i+1]:
                isSorted = False
                tempSortIndex = None
                a[i], a[i+1] = a[i+1], a[i]
            elif tempSortIndex is None:
                tempSortIndex = i
            print(f"{a}, {i}, {sortIndex}")
            # print(a)
        if tempSortIndex is not None:
            sortIndex = tempSortIndex

a = [500, 6, 2, 5, 20, 1, 17, 200, -4, -217]
sort(a)
print(a)
