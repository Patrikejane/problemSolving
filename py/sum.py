def SumsCount(n):
  if n <= 1:
    return 0
  sumsCount = 0
  # the first number i can be 1, 2, ..., n-1
  for i in range(2,n//2+1):
    # the rest must sum up to n-i
    # or the rest is just the number (n-i)
    sumsCount += SumsCount(n-i) + 1
    print(sumsCount)
  return sumsCount
print(SumsCount(8))
