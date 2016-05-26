T = int(input())
for i in range(T):
  X = input()
  count = 0
  for i in range(1,len(X)):
    if(X[i-1] == 'A' and X[i] == 'A'):
      count +=1
    if(X[i-1] == 'B' and X[i] == 'B'):
      count +=1
  print(count)
  
