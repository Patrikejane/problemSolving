def is_substring(A,B):
  count = 0
  for i in A:
    if i in B:
      count +=1
  if count == len(A):
    return True
  else:
    return False

file = open("A-small-attempt.in",'r')
l = int(file.readline())
temp = file.read().splitlines()
for i in range(l):
  print("CASE #"+str(i)+": ",end='')  
  B = temp[i]
  A = {"ZERO": 0, "ONE": 0, "TWO": 0, "THREE": 0, "FOUR": 0, "FIVE":0, "SIX":0, "SEVEN":0, "EIGHT":0, "NINE":0}
  C = {"ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
  D =[]
  for i in A:
    if (is_substring(i,B)):
      A[i] = 1
    
  for i in A:
    if A[i] == 1:
      D.append(C[i])
  
  
  for i in set(D):
    print(i,end='')
  print('')
    
