A = []
J =3
for i in range(65536,131072):
  if(bin(i)[-1]) == "1":
    A.append(bin(i)[2:])
   

D = []

def fact(x):
  for i in range(2, x):
    if(x % i) == 0:
      return i
  
def is_prime(x):
  if x == 2:
    return True
  return divmod(2 ** (x - 1), x)[1] == 1


B = [[] for x in range(len(A))]
for i in range(len(A)):
  for j in range(2,11):
    B[i].append(int(A[i],j))

C = [[] for x in range(len(A))]    
for i in range(len(B)):
  for j in range(9):
    if (is_prime(B[i][j])== True):
      C[i].append(1)
    else:
      C[i].append(0)


  
for i in range(len(C)):
  if(sum(C[i]) == 0):
    D.append(i)
    
for i in D:
  for j in range(9):
    C[i][j] = fact(B[i][j])

for i in range(J):
  out =""
  for j in C[D[i]]:
      out += str(j)+ " " 
  print(str(A[D[i]]) + " " + out)  
