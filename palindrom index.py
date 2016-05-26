T = int(input())
for i in range(T):
  strn = input()
  if strn[::-1] == strn:
      print('-1')
  else: 
      pointer,dev = 0,0
      while pointer<=len(strn) and dev==0:
          res=strn[:pointer]+strn[pointer+1:]
          #print(res)
          if res[::-1] == res :
              print (pointer)
              dev=1
          pointer=pointer+1
