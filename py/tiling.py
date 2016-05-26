n = 1000
mem = [0, 1, 1, 5, 11, 36,95]


def tiling(n):
  mem = [0, 1, 1, 5, 11, 36,95]
  print("fuk1")
  if n == 0:
    mem[0]=0
    print("fuk0")
  if n == 1:
    mem[1]=1
    print("fuk1")
  if n == 2:
    mem[2]=1
    print("fuk2")
  if n == 3:
    mem[3]=5
    print("fuk3")
  if n == 4:
    mem[4]=11
    print("fuk4")
  else:
    mem[n]= mem[n-1]+5*mem[n-2]+mem[n-3]+mem[n-4]
  return mem[n]


print(tiling(10))

''''
def Rectangles(n):
    
    a = c = d = 1
    b = 0   

    while n:
        n -= 1
        a, b, c, d = b, c, d, d + 5 * c + b - a
        d %= 1e9+7
        
    return c

''''
