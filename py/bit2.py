def fun(n):
  summ = 0
  num  = 0
  for i in range(n+1):
    if i == 0:
      num = 0
      summ+=num
    elif i == 1:
      num = 1
      summ+=num
    elif i %2 == 1:
      num = num
      summ += num
    else:
      num +=1
      summ += num
  return summ
        
