# p3

def naive(bids):
  def getDaySpan(bids):
    mina = None
    maxb = None
    for i in bids:
      if mina is None or i[0] < mina:
        mina = i[0]
      if maxb is None or i[1] > maxb:
        maxb = i[1]
    return mina, maxb

  minDay, maxDay = getDaySpan(bids)
  dayMaxFish = []
  for day in range(minDay, maxDay):
    maxFish = 0
    for bid in bids:
      if day >= bid[0] and day < bid[1] and bid[2] > maxFish:
        maxFish = bid[2]
    dayMaxFish.append((day, maxFish))
  dayMaxFish.append((maxDay, 0))
  return dayMaxFish


def merge(pi, pj):
  out = [(-float('Inf'), 0)]
  i, j = 0, 0
  while (i < len(pi) and j < len(pj)):
    if pi[i][0] < pj[j][0]:
      if (pi[i][1] > out[-1][1]):
        out.append(pi[i])
      i += 1
    else:
      if (pj[j][1] > out[-1][1]):
        out.append(pj[j])
      j += 1
  if i < len(pi):
    out += pi[i:]
  if j < len(pi):
    out += pj[j:]
  return out

def better(bids):
  if len(bids) == 1:
    bid = bids[0]
    return [(bid[0], bid[2]), (bid[1], 0)]
  
  bidi = bids[:len(bids)//2]
  bidj = bids[len(bids)//2:]
  ploti = better(bidi)
  plotj = better(bidj)
  return merge(ploti, plotj)


bids = [(0, 2, 1),\
        (1, 3, 2)]

print('p3 naive', naive(bids))

print('p3 n log n', better(bids))
