n = int(input())

for i in range(n):
  tacos = 0
  b = [int (x) for x in input().split()]
  a = b[1:] 
  t = b[0]
  if (a.count(0))> 2:
    print(0)
  else:

    a = sorted(a)
    #print(a)    
    maxx = a[2]
    mid = a[1]
    minn = a[0]
    
    if (maxx == mid ):
      val = minn // 2
      tacos = mid + val
        #print(minn,maxx,trd,a)
    elif( mid == minn ):
      val = maxx// 2
      tacos = mid + val

    elif( maxx == minn ):
      val = mid// 2
      tacos = maxx + val
      
    elif((maxx - mid) >= minn):
      tacos = mid + minn
        
    else:
      tacos = maxx
            
        
        #a[a.index(maxx[0])] += -1
        #a[a.index(mid[1])] += -1
        #tacos += 1
      
    if (tacos > t):
      print(t)
    else:
      print(tacos)
    
  
