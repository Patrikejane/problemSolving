def bleatrix(N):
  d = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
  trigger = 1

  def count(x):
    value = []
    for i in d.values():
      value.append(i)

    return value.count(0)

  for i in range(1,1000):
    trigger = i
    value= []
    n = N *i
    a = [int(i) for i in str(n)]
    for i in a:
      d[i] += 1
    if count(d) == 0:
      break
    
  if trigger == 999:
    return str("fuk")
  else:
    return n

    
''''
n = N*2

a = [int(i) for i in str(n)]
print (a)
for i in a:
  d[i] += 1

print(d)
if count(d) == 0:
  print(n)
n = N*3

a = [int(i) for i in str(n)]
print (a)
for i in a:
  d[i] += 1

print(d)
if count(d) == 0:
  print(n)

'''
  
  


  

