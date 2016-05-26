def maxprofit(array,n):
  reveneu = []
  for i in range(n):
    reveneu.append(0)
  #if (n == 1):
    #return array[n-1][2]
  for i in range(n):
        reveneu[i] = array[i][2]

  for i in range(1,n):
    revenu = array[i][2]
    currentprofit = array[n-1][2]
  
    val = myfunction(array,i)
  
    if(val != -1):
      revenu += reveneu[val]
    reveneu[i] = max(revenu,reveneu[i-1])
  
  return reveneu[n-1]
  

def myfunction(array,i):
  for j in range (i-1,-1,-1):
    if (array[j][1] <= array[i][0]):
      return j
  return -1




In = int(input())

for i in range(In):
  jobs = []

  T = int(input())
  for j in range(T):
    INvals = [int(x) for x in input().split()]
    jobs.append(INvals)

  jobs = sorted(jobs, key = lambda x :x[1])
  print(maxprofit(jobs,len(jobs)))
  #print(jobs)
  
  
  
 
    
    
    
