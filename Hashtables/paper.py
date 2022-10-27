# hashTable = []

def hash(i):
    hashCode = (2*i + 3) % 17
    # hashTable.append(hashCode)
    return hashCode

def run():
    for i in (36, 88, 54, 28, 49, 21, 63, 7, 19, 2, 11, 41, 34):
        out = hash(i)
        print(out)

run()

# print(hashTable)