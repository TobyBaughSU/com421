def sort(a: list):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        print(a)

a = [500, 6, 2, 5, 20, 1, 17, 200, -4, -217]
sort(a)
print(a)
