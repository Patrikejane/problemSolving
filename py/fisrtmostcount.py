def FindTheSame(s):
    for i in s:
        x = s.count(i)
        if x > 1:
            break
    if x > 1:
      return i*x
    else:
      return ""

print(FindTheSame("abdDcef"))
