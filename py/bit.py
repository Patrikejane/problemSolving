def fun(n):
  temp = []
  for i in range(0,n+1):
    if i == 0:
      temp.append(0)
    elif i == 1:
      temp.append(1)
    elif i%2 == 1:
      temp.append(temp[i-1])
    else:
      temp.append(temp[i-1]+1)
      
  print (sum(temp))
