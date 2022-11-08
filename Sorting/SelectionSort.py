def sort(a: list):
    for i in range(len(a)-1):
        smallest = i
        for j in range(i+1, len(a)):
            if a[j] < a[smallest] or smallest == i:
                smallest = j
        if a[smallest] < a[i]:
            a[smallest], a[i] = a[i], a[smallest]
        print(a)


a = [500, 6, 2, 5, 20, 1, 17, 200, -4, -217]
# a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sort(a)
print(a)
