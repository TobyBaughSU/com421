class Queue:

    def __init__(self, size):
        self.array = [None] * size
        self.size = size
        self.start = 0
        self.next = 0

    def __str__(self):
        return f"{self.array.__str__()}, {str(self.array[self.start])}, {str(self.array[self.next])}"

    def to_list(self):
        out = []
        for i in range(self.size):
            if self.array[(i + self.start) % self.size] is None:
                break
            out.append(self.array[(i + self.start) % self.size])

        return out

    def add(self, *items):
        for i in items:
            if self.array[self.next] is not None:
                raise IndexError
            self.array[self.next] = i
            self.next = self.increment_count(self.next)

    def remove(self, count=1):
        item = [None] * count
        for i in range(count):
            item[i] = self.array[self.start]
            self.array[self.start] = None
            self.start = self.increment_count(self.start)
        if count == 1:
            item = item[0]
        else:
            item = tuple(item)
        return item

    def increment_count(self, counter):
        # if counter < self.size - 1:
        #     counter += 1
        # else:
        #     counter = 0#
        counter += 1
        counter %= self.size
        return counter

    def peak(self):
        return self.array[self.start]


a = Queue(5)
a.add("how", "goes", "thee", "in", "this")
print(a)
# print(a.to_list())

print(a.remove(3))
a.add("place")
print(a)
# print(a.to_list())
print(a.remove(3))

print(a)
