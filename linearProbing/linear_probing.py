import matplotlib.pyplot as plt
import numpy as np
import random
import math

class HashingTableLP(object):

    def __init__(self):
        self.max_length = 337
        self.length = 0
        self.table = [None] * self.max_length
        self.step = 0

    def __len__(self):
        return self.length

    def __setitem__(self, key):
        self.length += 1
        self.step = 1
        hashed_key = self._hash(key)
        while self.table[hashed_key] is not None:
            hashed_key = self._rehash_key(hashed_key)
            self.step +=1
            #if self.table[hashed_key] == key:
                #self.length -= 1
                #break
        self.table[hashed_key] = key

    def _hash(self, key):
        # TODO more robust
        return key % self.max_length

    def _rehash_key(self, key):
        return (key + 1) % self.max_length

# def generateD():  #this method was used to generate data file,
    # file = open('Data1.txt', 'w')
    # for i in range(330):
    #     file.write(str(random.randint(10, 5000)) + '\n')
    # file.close()

    # file = open('DATA2.txt', 'w')
    # for i in range(197):
    #     file.write(str(random.randint(10, 1500)) + '\n')
    # file.close()

    # file = open('DATA3.txt', 'w')
    # for i in range(87):
    #     file.write(str(random.randint(10, 3000)) + '\n')
    # file.close()

def plott(x,y):
    plt.plot(x, y, color='red')
    plt.xlabel('1/(1-alpha)')
    plt.ylabel('Number of Probes')
    plt.title('Linear Probing')
    plt.legend()
    plt.show()

    m, mm = np.polyfit(np.log10(x), np.log10(y), 1)

    line_xs = np.array([1, 2])
    line_ys = m * line_xs + mm

    plt.loglog(10 ** (line_xs), 10 ** (line_ys), '--', label='m=%.2f' % m, color='red')
    plt.legend()
    plt.show()


h = HashingTableLP()
a = []
b = []
# generateD() #USED TO GENERATE DATA


file = open('DATA3.txt','r')#Data1 corresponds to alpha=1, DATA2 corresponds to alpha=0.5 and DATA3 corresponds to alpha ~0.2

for i in file:
   i = i.rstrip()
   i = int(i)
   h.__setitem__(i)
   a.append((1/(1-(h.length/h.max_length))))
   b.append(h.step)


file.close()

plott(a,b)