import matplotlib.pyplot as pl

def greed(tuples, Q):
  # tuples is a list of (fi, ti, qi)
  tuples = sorted(tuples, key=lambda tup: tup[1], reverse=True)
  sumq = 0
  out = []
  idx = 0
  while sumq < Q:
    f, t, q = tuples[idx]
    if sumq+q <= Q:
      out.append((f, q))
      sumq += q
      idx += 1
    else:
      out.append((f, Q-sumq))
      sumq = Q
  return out

def turkeys(turs):
  # turs is a list of turkeys [(a1, b1), (a2, b2),...]. 1-based numbering
  turs = sorted(turs, key=lambda tup: tup[1])
  t = [-float('inf')]  # message times. 1-based numbering
  for i in range(len(turs)):
    if turs[i][0] > t[-1]:
      t.append(turs[i][1])
  return t

foodList = [('fish', 5, 8),
            ('beef', 6, 3),
            ('port', 2, 10),
            ('chicken', 3, 13),
            ('turkey', 4, 11),
            ('steak', 8, 1),
            ('sushi', 7, 2)]

print(greed(foodList, 20))

turs = [(2, 8),
        (10, 16),
        (3, 4),
        (1, 7),
        (5, 13),
        (9, 12),
        (11, 15),
        (13, 14),
        (7, 11),
        (5, 9),
        (12, 18)]

msgTimes = turkeys(turs)
#print(msgTimes)

pl.figure(0)
for i, ts in enumerate(turs):
  pl.plot(ts, [i, i])
for mt in msgTimes:
  pl.plot([mt, mt], [0, len(turs)-1])
pl.xlabel('time')