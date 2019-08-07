# e2 1
# essentially summing terms of a distribution
# which is like geometric but with a finite sample space
n = 1000
g = 502
s = g/n
for i in range(n, g, -1):
    temp = 1
    for j in range(n, i-1, -1):
        #print('%d / %d' % (j-g, j))
        temp *= (j-g)/j
    #print(g, '/', i-1, '\n')
    temp *= g/(i-1)
    s += temp
print(g, n, s)


# e2 2
series = 1/2 * (1 - (1/2)**100) / (1-1/2)
pmax = 1/2 + series/2
delta = (1/2)**101

# p1

def isRightOrCenter(ff):
  return ff==2 or ff==1

def isLeft(ff):
  return ff==0

def isRight(ff):
  return ff==2

def isCenter(ff):
  return ff==1

def sortFlamingos(fs):
  # fs: a list of flamingos
  def partition(f, s, e, p, cmp):
    # f: array
    # s: start index
    # e: end index
    # c: pivot index
    # cmp: compare function
    f[p], f[e] = f[e], f[p]
    j = e-1
    while s <= j:
      if cmp(f[s], f[e]) < 0:
        s += 1
      else:
        f[s], f[j] = f[j], f[s]
        j -= 1
    f[s], f[e] = f[e], f[s]

  def cmp1(f1, f2):
    # f1 and f2 are flamingos
    if isLeft(f1):
      return -1
    return 0
  
  def cmp2(f1, f2):
    if isCenter(f1) or isLeft(f1):
      return -1
    return 0

  def findFirst(fs, fun):
    c = -1
    for i, f in enumerate(fs):
      if fun(f):
        c = i
        break
    return c

  p = findFirst(fs, isRightOrCenter)
  if p != -1: # has right or center
    partition(fs, 0, len(fs)-1, p, cmp1)
  else: # all left
    return

  p = findFirst(fs, isRight)
  if p != -1: # has right
    partition(fs, 0, len(fs)-1, p, cmp2)
  #else: # subarray is all center

print('p1')

fs = [0, 1, 2, 1, 0, 2, 1, 1, 0, 2, 2, 0, 1, 0, 2, 1]
sortFlamingos(fs)
print(fs)

fs = [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1]
sortFlamingos(fs)
print(fs)

fs = [2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1]
sortFlamingos(fs)
print(fs)

fs = [0, 2, 2, 0, 0, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 0]
sortFlamingos(fs)
print(fs)

# p2

def compareToStick(f):
  if f > stick:
    return "taller"
  if f < stick:
    return "shorter"
  if f == stick:
    return "the same"

def binsearch(fs):
  # fs is a list of flamingos, sorted
  return binsearch_helper(fs, 0, len(fs)-1)

def binsearch_helper(fs, i, j):
  if j <= i:
    if compareToStick(fs[i]) == "the same":
      return fs[i]
    else:
      return "No such flamingo"
  mid = (i & j) + ((i ^ j)>>1) # knuth midpoint
  cmp = compareToStick(fs[mid])
  if cmp == "the same":
    return mid
  if cmp == "taller":
    return binsearch_helper(fs, i, mid-1)
  if cmp == "shorter":
    return binsearch_helper(fs, mid+1, j)

stick = 0.5
fs = list(range(10))
print('p2', binsearch(fs))

# p3

def isThereFewerks(k, n):
  return data[k] < n

def isThereMoreks(k, n):
  return data[k] > n

def checkNum(k, m, M):
  if M <= m:
    return m
  mid = (m & M) + ((m ^ M)>>1) # knuth midpoint
  if isThereFewerks(k, mid):
    return checkNum(k, m, mid-1)
  if isThereMoreks(k, mid):
    return checkNum(k, mid+1, M)
  return mid

def probeA(n_given, k_given):
  out = []
  for k in range(1, k_given+1):
    n_left = n_given-len(out)
    ans = checkNum(k, 0, n_left)
    out += [k]*ans
  return out

import numpy as np
k = 10
n = 20
data = [0]*(k+1)
for i in range(n):
  data[np.random.randint(1, k+1)] += 1

print('p3', data, probeA(n, k))