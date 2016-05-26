In = int(input())

for i in range(In):
  A = input()
  pat = ""
  i = 0
  pat += A[0]
  while (i <len(A)):
    shift = 0
    if 




  
print(A,pat)


'''def KnuthMorrisPratt(text, pattern):

    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
        print(shift)
        print(shifts)
        

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        print(matchLen)
        if matchLen == len(pattern):
            return startPos
    

A = "SunimalSunimalSunimalSunimalSunimalSunimalSunimal"
B = "Sunimal"

print(KnuthMorrisPratt(A, B))'''



































