import heapq

n = int(input())

for i in range(n):
  tacos = 0
  b = [int (x) for x in input().split()]
  a = b[1:] 
  t = b[0]
  if (a.count(0))> 2:
    print(0)
  else:
    while(a.count(0) < 2):
      maxx = heapq.nlargest(1, a)
      mid = heapq.nlargest(2, a)
      minn = heapq.nlargest(3, a)
      if (maxx[0] == mid[1] ):
        val = trd[3] // 2
        tacos += mid[1] + val
        print(minn,maxx,trd,a)
      else if(mid[1] == minn[3] ):
        val = maxx[0] // 2
        tacos += mid[1] + val
        
      else:
        a[a.index(maxx[0])] += -1
        a[a.index(mid[1])] += -1
        tacos += 1
      
    if (tacos > t):
      print(t)
    else:
      print(tacos)
    
  
  

  

  

#res = heapq.nlargest(2, some_sequence)
#print res[1]
