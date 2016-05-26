In = input().split()

N = int(In[0])
Y = int(In[1])

memo = [[None for i in range(Y)]for j in range(N)]



for i in range (0,N):
      for j in range (0,Y):
        memo[i][j] = 0 

for i in memo:
    print(i)


for i in range(int(input())):
  summ=0
  a = input().split()
  if a[0] == 'a':
    for i in range (int(a[1])-1,int(a[3])):
      for j in range (int(a[2])-1,int(a[4])):
        memo[i][j] +=1

  if a[0] == 'r':
    for i in range (int(a[1])-1,int(a[3])):
      for j in range (int(a[2])-1,int(a[4])):
        memo[i][j] -=1
  if a[0] == 'q':
    for i in range (int(a[1])-1,int(a[3])):
      for j in range (int(a[2])-1,int(a[4])):
        summ += memo[i][j]
    print(summ)
        
  

for i in memo:
    print(i)
