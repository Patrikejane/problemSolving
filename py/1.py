__author__ = 'Smalkakulage'


T=int(input())
n,d,k = input().split()
list1=[]
x=0
eatdish=[]
for i in range(int(n)):
    list1.append(input().split(' '))

c=0
for i in list1:
    x += float(i[c])
    eatdish.append(c+1)
    c+=1
    
    
x==x/int(d)

print (x)
print ('\n')
print (eatdish )    

        
    
