
cyclend = None
cyclsrt = None

edges = []

def cycle_exists(G):                     # - G is a directed graph
    color = {u : "white" for u in G}  # - All nodes are initially white
    parent = {u : "None" for u in G}
    edge = []
    found_cycle = [False]                
                                         
                                         
    for u in G:                          
        if color[u] == "white":
            dfs_visit(G, u, color, found_cycle,parent)
        if found_cycle[0]:
            break
    return found_cycle[0],parent
#-------
 
def dfs_visit(G, u, color, found_cycle,parent):
   
    global cyclsrt
    global cyclend
    if found_cycle[0]:                          # - Stop dfs if cycle is found.
        return
    color[u] = "gray"                          
    for v in G[u]:                             
        if color[v] == "gray":
            
            cyclsrt = u
            cyclend = v
            found_cycle[0] = True
            return
        if color[v] == "white":                 
            parent[v] = u
            
            dfs_visit(G, v, color, found_cycle,parent)
    color[u] = "black"                         


n = int(input())
for i in range(n):
    x = [int(x) for x in input().split()]
    edges.append(x)

graph = dict()

for i in range(1,n+1):
    graph[i]=[]

#print(graph)
#print(edges)

for i in range(1,len(edges)+1):
    graph[i].append(edges[i-1][0])
    
'''graph_example_1 = { 
                    1 : [3],
                    2 : [1],
                    3 : [2],
                    }'''
(state,graphX) = cycle_exists(graph)

listsum = []

if state == True:
    
      #print ("cycle")
      current = cyclsrt
      while current != cyclend:
          listsum.append(current)
          
          #print(current,end = " ")
          current = graphX[current]
      listsum.append(current)
      #print(current,end = " ")

      summ = 1
      present = 100**len(listsum)
      for i in listsum:
          for j in edges:
              if i in j:
                  summ *= j[1]
          
      result = summ / present
      print("%.2f" % result)

else:
  print("fuk you")




  
