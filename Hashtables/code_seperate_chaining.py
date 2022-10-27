hashTable = {}

def hash(key):
    hashCode = ord(key) % 127
    hashTable[hashCode].append(key)

