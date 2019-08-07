# e2a
def LIS(A):
  #A[0]~A[n-1] is the input sequence
  D = [1]
  for i in range(1, len(A)):
    d = 1
    for k in range(0, i):
      if A[k] < A[i] and D[k]+1 > d:
        d = D[k]+1
    D.append(d)
  # find max in D
  m = 0
  for i in range(len(A)):
    if D[i] > m:
      m = D[i]
  return m

# e2b
def LIS_(A):
  #A[0]~A[n-1] is the input sequence
  D = [1]
  prev = [-1]
  for i in range(1, len(A)):
    d = 1
    kbest = -1
    for k in range(0, i):
      if A[k] < A[i] and D[k]+1 > d:
        d = D[k]+1
        kbest = k
    D.append(d)
    prev.append(kbest)
  # find max in D
  m = 0
  ibest = -1
  for i in range(len(A)):
    if D[i] > m:
      m = D[i]
      ibest = i
  # trace LIS
  out = []
  while ibest != -1:
    out.append(A[ibest])
    ibest = prev[ibest]
  return m, out[::-1]

# e2 additional
import bisect
def fredman(A):
  S = []
  X = []
  p = [-1]*len(A)
  for i in range(len(A)):
    x = bisect.bisect_left(S, A[i])  # insertion point
    if x == len(S):
      S.append(A[i])
      X.append(i)
      if len(S)>1:
        p[i] = X[-2]
    else:
      if A[i] < S[x]:
        S[x] = A[i]
        X[x] = i
        if x > 0:
          p[i] = X[x-1]
  # reconstruct
  curr = X[-1]
  LIS = [A[curr]]
  while p[curr] != -1:
    curr = p[curr]
    LIS.append(A[curr])
  return len(S), LIS[::-1]

A = [2, 6, 3, 4, 1, 2, 9, 5, 8, -1, 0, 1, 2]
print('e2fred', fredman(A))

A = [2, 6, 3, 4, 1, 2, 9, 5, 8, -1, 0, 1, 2]
print('e2a', LIS(A))

A = [2, 6, 3, 4, 1, 2, 9, 5, 8, -1, 0, 1, 2]
print('e2b', LIS_(A))

# p1c

def memoization(n, S):
  # initialize memo
  memo = [-1]*(n+1)
  memo[0] = 0
  for i in range(1, n+1):
    if i < min(S):
      memo[i] = None
    else:
      break
  return helper(n, S, memo)

def helper(k, S, memo):
  if memo[k] != -1:
    return memo[k]
  candidates = []
  for s in S:
    if k-s >= 0:
      cand = helper(k-s, S, memo)
    if cand is not None:
      candidates.append(cand+1)
  memo[k] = min(candidates)
  return memo[k]

# p1d

def dp(n, S):
  # initialize array
  sol = [None]*(n+1)
  sol[0] = 0
  # crawl
  for k in range(min(S), n+1):
    candidates = []
    for s in S:
      if k-s >= 0 and sol[k-s] is not None:
        candidates.append(sol[k-s]+1)
    sol[k] = min(candidates)
  return sol[n]

S = {1, 4, 7}
n = 10

print('p1c', memoization(n, S))

print('p1d', dp(n, S))

# p2

def river(Q):
  # initialization
  X = [None]*len(Q) # answer array
  p = [0]   *len(Q) # "picked". for backtrack
  if Q[0] > 0:
    X[0] = Q[0]
    p[0] = 1
  else:
    X[0] = 0
  if Q[1] > X[0]:
    X[1] = Q[1]
    p[1] = 1
  else:
    X[1] = X[0]
  # crawl
  for k in range(2, len(Q)):
    if Q[k]+X[k-2] > X[k-1]:
      X[k] = Q[k]+X[k-2]
      p[k] = 1
    else:
      X[k] = X[k-1]
  # backtrack
  ans = []
  k = len(Q)-1
  while k >= 0:
    if p[k] == 1:
      ans.append(k)
      k -= 2
    else:
      k -= 1
  return X[-1], ans[::-1]

Q = [21, 4, 6, 20, 2, 5]
print('p2', river(Q))

# p3a

def linear(B):
  Aprev = B[0]
  Amax = Aprev
  kAmax = 0
  s = [1]*len(B) # single-element subarray?
  for k in range(1, len(B)):
    Acurr = B[k]
    if Aprev > 0:
      Acurr += Aprev
      s[k] = 0
    if Amax < Acurr:
      Amax = Acurr
      kAmax = k
    Aprev = Acurr
  kmin = kAmax
  while True:
    if s[kmin] == 1:
      return Amax, kmin, kAmax
      # covers all situations. s[0] is always 1
    kmin -= 1

B = [2, -1, 3, -5]
print('p3a', linear(B))

# p3b

def getD(A, n):
  # initialize 4d
  D=[[[[None for i in range(n)]\
       for j in range(n)]\
      for k in range(n)]\
     for l in range(n)]
  # crawl
  for x in range(n):
    for y in range(n):
      D[x][y][x][y] = A[x][y]
      for j in range(y+1, n):
        D[x][y][x][j] = D[x][y][x][j-1] + A[x][j]
      for i in range(x+1, n):
        D[x][y][i][y] = D[x][y][i-1][y] + A[i][y]
      for i in range(x+1, n):
        for j in range(y+1, n):
          D[x][y][i][j] = D[x][y][i][j-1] + D[x][y][i-1][j] - D[x][y][i-1][j-1]\
                          + A[i][j]
  return D

def maxD(D, n):
  DD = D[0][0][0][0]
  xx, yy, ii, jj = 0, 0, 0, 0
  for x in range(n):
    for y in range(n):
      for i in range(x, n):
        for j in range(y, n):
          if D[x][y][i][j] > DD:
            DD = D[x][y][i][j]
            xx = x
            yy = y
            ii = i
            jj = j
  return xx, yy, ii, jj

A = [[2,3,10,0],
     [3,-2,0,-1],
     [-1,2,-5,-2],
     [-1,2,-5,-2]]
D = getD(A, 4)
print('p3b p3c', maxD(D, 4))

# p3d

def getE(A, n):
  # initialize 3d
  E=[[[None for i in range(n)]\
      for j in range(n)]\
     for k in range(n)]
  # crawl E
  for y in range(n):
    for x in range(n):
      E[x][x][y] = A[x][y]
      for i in range(x+1, n):
        E[x][i][y] = E[x][i-1][y] + A[i][y]
  return E

def n3(E, n):
  # returns best of s, x, a, i, b
  # s: quality seen among all (x, i)
  # a, b: as in (a)
  bestA, bestx, besti, besta, bestb = [None]*5
  for x in range(n):
    for i in range(x, n):
      A, a, b = linear(E[x][i][:])
      # note if using E[x][y][i] ordering, E[x][:][i] is wrong
      if bestA is None or A > bestA:
        bestA = A
        besta = a
        bestb = b
        bestx = x
        besti = i
  return bestA, bestx, besta, besti, bestb

A = [[2,3,10,0],
     [3,-2,0,-1],
     [-1,2,-5,-2],
     [-1,2,-5,-2]]
E = getE(A, 4)
print('p3d', n3(E, 4))