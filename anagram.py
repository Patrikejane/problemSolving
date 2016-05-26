from collections import Counter
T = int(input())
for i in range(T):
    strn = input()
    lnth = len(strn)
    if lnth % 2 == 1:
        print(-1)
    else:
        count = 0
        s1= Counter(strn[:lnth//2])
        s2 = Counter(strn[lnth//2:])
        #print(s1,s2)
        for j in s2:
            #print(j,"#")
            diff = s2[j] - s1.get(j,0)
            #print(diff,s1.get(j,0),"*")
            if diff > 0:
                count += diff
        print(count)
