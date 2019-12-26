import math
import random
import matplotlib.pyplot as plt
import numpy as np


class cuckoo:

    def __init__(self):
        self.table_length = 41
        self.key_array = []
        self.table = [[-1] * 2 for i in range(self.table_length)]
        print(self.table)
        self.step = 1
        self.f = 0
        self.r = 0

    def get_hash(self, key, next):
        if next is 0:
            return (key + self.r) % self.table_length
        else:
            return ((key + self.r) // self.table_length) % self.table_length

    def set(self, key):
        self.step = 1
        count = 1
        current_key = key
        actual_key = key
        next = 0
        self.f = 0
        while True:
            if next is 0:
                index = self.get_hash(current_key, next)
                current_key, self.table[index][0] = self.table[index][0], current_key
                self.step += 1
                next = 1
            elif next is 1:
                index = self.get_hash(current_key, next)
                current_key, self.table[index][1] = self.table[index][1], current_key
                self.step += 1
                next = 0

            if current_key == -1:
                break

            if actual_key == current_key:
                count += 1

            if count >= 3:
                self.f = 1
                break
        return self.f

    def rehash(self):
        self.r += 2
        self.table = [[-1] * 2 for i in range(self.table_length)]
        for i in range(0, len(self.key_array)):
            self.f = self.set(self.key_array[i])
            if self.f == 1:
                self.rehash()



a, b = [], []

c = cuckoo()

fill_length = 1
file = open("test.txt", "r")
for i in file:
    fill_length += 1
    i = i.rstrip()
    c.key_array.append(int(i))
    value = c.set(int(i))

    if value == 1:
        c.rehash()

    a.append(c.step)
    b.append(((fill_length / (2.0 * c.table_length))))

file.close()

x = a
y = b
plt.plot(y, x, color='red')
plt.xlabel('alpha')
plt.ylabel('Number of probes')
plt.title('Cuckoo Hashing')
plt.legend()
plt.show()

m, b = np.polyfit(np.log10(x), np.log10(y), 1)

line_xs = np.array([1, 2])
line_ys = m * line_xs + b

plt.loglog(10 ** (line_xs), 10 ** (line_ys), '--', label='m=%.2f' % m, color='red')
plt.legend()
plt.show()
