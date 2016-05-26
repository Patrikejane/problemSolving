time = input().strip()
x = time[8:]
y = time[:2]
if x =="PM":
  if( y == '12'):
    print(time[0:8])
  else:
    ss = str(int(y) + 12)
    print(ss + time[2:8])


elif x =="AM":
  if( y == '12'):
    print('00' + time[2:8])
  else:
    print(time[0:8])


