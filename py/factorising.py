def many_ways_not_one(n):
  count = 0
  i = 2
  while (i < n/2):
    print(i)
    count += 1
    i += 1

  for j in range(2,(n//2)+1):
    for x in range(j,(n//2)+1):
      if j * x == n or j +x == n:
        #print(j,x)
        count +=1
      
    
  return count
      
  

print(many_ways_not_one(1000))
