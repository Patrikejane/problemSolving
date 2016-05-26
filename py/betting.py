from math import log

def compare(array, c1, c2):
    x , y = array[c1], array[c2]
    if (x < y):
        y = y-x
        x = 2*x
    else:
        x = x - y
        y = 2 * y
    arrayx = array[:]
    arrayx[c1], arrayx[c2] = x , y
    return arrayx

def backtrack(index):
    c = index
    if index == 0:
        return 0
    if index < 4:
        return 0
    else:
        return(index//3)
        
def track(array,index):
    tracks = []
    x = index
    tracks.append(x)
    while(x != 0):
        x = backtrack(x)
        tracks.append(x)
    tracks.reverse()
    
    tracked = []
    
    for i in tracks:
        tracked.append(array[i])
    depth = len(tracked)
    last = tracked[depth -1]
    blast = tracked[depth - 2]
    zindex = last.index(0)
    if (zindex < 2 and blast[zindex] == blast[zindex +1]):
        tracked.pop()
        last[zindex], last[zindex + 1] = last[zindex + 1], last[zindex]
        tracked.append(last)
    for i in tracked:
        printer = [str(j) for j in i]
        print(" ".join(printer))
        
line = input().split()
a,b,c = int(line[0]), int(line[1]), int(line[2])
x = [a, b, c]
L = [x]


b = 0
n = 0
while(b < 12):
    
    cash = L[n]
    comp1 = compare(cash, 0, 1)
    comp2 = compare(cash, 1, 2)
    comp3 = compare(cash, 0, 2)
    x1 = len(L)
    L.append(comp1)
    x2 = len(L)
    L.append(comp2)
    x3 = len(L)
    L.append(comp3)

    no_1 = comp1.count(0)
    no_2 = comp2.count(0)
    no_3 = comp3.count(0)

    if(no_1 != 0 or no_2 != 0 or no_3 != 0):
        
        if (no_1 != 0):
            x = x1
        elif (no_2 != 0):
            x = x2
        else:
            x = x3
        track(L,x)
        break
            
    else:
        if(n== 0):
            b =1
        elif(int(log(n, 3)) != b):
            b+= 1
        n += 1
if b>= 12:
    print("Ok")
