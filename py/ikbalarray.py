NQ = [int(x) for x in input().split()]

N = NQ[0]
Q = NQ[1]

a = [0]*N
b = [0]*N


def fun1(l,r,c):
  for i in range(l-1,r):
    a[i] += c
  #print(a)
  #print(b)

def fun2(l,r,c):
  for i in range(l-1,r):
    b[i] += c
  #print(b)

def fun3(l,r):
  summ=0
  for i in range(l-1,r):
    summ += a[i]*b[i]
  print(summ % 1000000007)


for i in range(Q):
  expression = input().split()
  if expression[0] == '1':
    fun1(int(expression[int(1)]),int(expression[2]),int(expression[3]))
  elif expression[0] == '2':
    fun2(int(expression[int(1)]),int(expression[2]),int(expression[3]))
  elif expression[0] == '3':
    fun3(int(expression[int(1)]),int(expression[2]))
  else:
    print ("sunimal")
