Nnodes = int(input())
d = {}
tokens = [int(x) for x in input().split()]

for i in range (Nnodes):
  d[i] = tokens[i]

adjeclist = [[] for i in range(Nnodes)]

for i in range(Nnodes-1):
  edges = [int(x) for x in input().split()]
  adjeclist[edges[0]-1].append(edges[1])

for i in range(Nnodes):
  print(i,adjeclist[i])
  
  
