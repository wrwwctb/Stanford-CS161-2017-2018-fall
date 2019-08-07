import numpy as np
def toadToToadComparison(toad1, toad2):
  '''
  input: two toads
  output tuple: (what toad2 says about toad1,
                 what toad1 says about toad2)

  toad1        toad2         output
  trustworthy  trustworthy   (1, 1)
  trustworthy  tricky        (1, 0) or (0, 0)
  tricky       trustworthy   (0, 1) or (0, 0)
  tricky       tricky        (1, 1), (1, 0), (0, 1) or (0, 0)
  '''
  if toad1 == 1:
    if toad2 == 1:
      return (1, 1)
    if toad2 == 0:
      if np.random.random() > .5:
        return (0, 0)
      else:
        return (1, 0)
  else:
    if toad2 == 1:
      if np.random.random() > .5:
        return (0, 0)
      else:
        return (0, 1)
    else:
      if np.random.random() > .5:
        if np.random.random() > .5:
          return (1, 0)
        else:
          return (0, 1)
      else:
        if np.random.random() > .5:
          return (1, 1)
        else:
          return (0, 0)

def toadToToadComparison_no_rand(toad1, toad2):
  if toad1 == 1:
    if toad2 == 1:
      return (1, 1)
    if toad2 == 0:
      return (0, 0)
  else:
    if toad2 == 1:
      return (1, 0)
    else:
      return (1, 1)

# p2a

def naive(toads):
  #input: a list of toads
  #output: a list of trustworthy toads
  nn = len(toads)
  comp = np.zeros((nn, nn), dtype=int) # all toad-to-toad comparisons
  for i in range(nn):
    for j in range(nn):
      if i == j:
        comp[i, i] = 0
        continue
      temp = toadToToadComparison(toads[i], toads[j])
      comp[i, j] = temp[0]
      comp[j, i] = temp[1]
  outputList = []
  for i in range(nn):
    if sum(comp[i, :]) >= nn//2:
      outputList.append(i)
  #print(comp)
  return outputList

toads = [0, 0, 0, 0, 1, 1, 1, 1, 1]
print('p2a', naive(toads))

## these use n comparisons
## p2b
#
#def divide(toads):
#  nn = len(toads)
#  # base cases
#  if nn == 1:
#    return
#  if nn == 2:
#    del toads[0]
#    return
#
#  def crawl(toads, i0, nn):
#    i = i0
#    while(len(toads) > nn//2 and i < len(toads)-1):
#      if toadToToadComparison(toads[i], toads[i+1]) != (1, 1):
#        del toads[i+1]
#        del toads[i]
#        if i > i0:
#          i -= 1
#      else:
#        i += 1
#
#  crawl(toads, 0, nn)
#  if len(toads) > nn/2:
#    del toads[len(toads)//2:]
#
## p2d
#
#def findOne(toads):
#  while (len(toads)>1):
#    divide(toads)
#  return toads[0]



def testDivide(seed, num, toads, divideFun):
  np.random.seed(seed)
  n0 = len(toads)
  for i in range(num):
    toads1 = list(np.random.permutation(toads))
    divideFun(toads1)
    #print('p2b', toads)
    # check
    nn = len(toads1)
    ss = sum(toads1)
    if nn == 0 or ss <= .5 * nn or nn > int(np.ceil(n0/2)):
      print('error:', i, ss, nn)
      return
  print('no error found')

def testFindOne(seed, num, toads, findFun):
  np.random.seed(seed)
  for i in range(num):
    toads1 = list(np.random.permutation(toads))
    toad = findFun(toads1)
    if toad != 1:
      print('error:', i)
      return
  print('no error found')


#print('p2b')
#testDivide(512, 100000, [0, 0, 0, 0, 1, 1, 1, 1, 1, 1], divide)
#
#print('p2d')
#testFindOne(512, 100000, [0, 0, 0, 0, 1, 1, 1, 1, 1, 1], findOne)


def divide_even(toads):
  if len(toads) == 2:
    del toads[0]
  for i in range(len(toads)-2, -1, -2):
    if toadToToadComparison(toads[i], toads[i+1]) == (1, 1):
      del toads[i]
    else:
      del toads[i:i+2]

def divide_odd(toads):
  if len(toads) == 1:
    return
  for i in range(len(toads)-2, 0, -2):
    if toadToToadComparison(toads[i], toads[i+1]) == (1, 1):
      del toads[i]
    else:
      del toads[i:i+2]
  if len(toads)%2 == 0:
    del toads[0]

def findOneEvenOdd(toads):
  while len(toads) > 1:
    if len(toads)%2:
      divide_odd(toads)
    else:
      divide_even(toads)
  return toads[0]

print('p2b')
testDivide(512, 100000, [0, 0, 0, 0, 1, 1, 1, 1, 1, 1], divide_even)

print('p2c')
testDivide(512, 100000, [0, 0, 0, 0, 1, 1, 1, 1, 1], divide_odd)

print('p2d')
testFindOne(512, 100000, [0, 0, 0, 0, 1, 1, 1, 1, 1, 1], findOneEvenOdd)
testFindOne(512, 100000, [0, 0, 0, 0, 1, 1, 1, 1, 1], findOneEvenOdd)