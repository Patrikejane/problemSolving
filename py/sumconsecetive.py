def SumOfConsecutiveNumbers(numArray):
    s = 0
    for i in range(len(numArray)-1):
        if numArray[i+1] == numArray[i]+1:
          s += numArray[i]
 

print(SumOfConsecutiveNumbers([1,2,3,4,6,8,9]))
