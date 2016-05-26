dictionary = {}

temp = [int(x) for x in input().split()]
N = temp[0]
Q = temp[1]


modVal = 1000000007

for i in range(2):
    dictionary[i + 1] = [0]*N
  

def func1(l, r, t):
    for i in range(l - 1, r):
        dictionary[1][i] += t

def func2(l, r, t):
    for i in range(l - 1, r):
        dictionary[2][i] += t

def func3(l, r):
  summ = 0
  for i in range(l - 1, r):
    summ += dictionary[1][i]*dictionary[2][i]
  print(summ)


for j in range(Q):
    init = [int(x) for x in input().split()]

    selector = init[0]

    if selector == 1:
        func1(init[1], init[2],init[3])
    elif selector == 2:
        func2(init[1], init[2],init[3])
    elif selector == 3:
        func3(init[1], init[2])
  
