def NumberofZeros(n):
  product = 1
  for i in range(n):
    product *= i+1
  x = str(product)
  count=0
  for i in range(len(x)-1, 0, -1):
    if x[i] == '0':
      count += 1
    else:
      break
  print(count)
  
NumberofZeros(10000)
