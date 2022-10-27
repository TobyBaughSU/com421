hashTable = {}

def hash(i):
    hashCode = (2*i + 3) % 17

    while True:
        try:
            hashTable[hashCode]
        except KeyError:
            hashTable[hashCode] = i
            break
        else:
            hashCode += 1

    return hashCode

def run():
    for i in (36, 88, 54, 28, 49, 21, 63, 7, 19, 2, 11, 41, 34):
        print(hash(i))

run()

print(hashTable)