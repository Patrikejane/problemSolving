primes = lambda q: (i for i in range(1,q) if i not in [j*k for j in range(1,int(round(math.sqrt(i)+1))) for k in range(1,int(round(math.sqrt(i)+1)))])
for i in primes(10):
   print (i),
