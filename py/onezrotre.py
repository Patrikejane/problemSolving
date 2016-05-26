

def one_zero_tree(N, K):
    stringone = "1"
    stringtwo = "" 
    i = 0
    while (i < N-1):
        for j in stringone:
            if j == '1':
                stringtwo += "10"
            else:
                stringtwo += "01"
        stringone = stringtwo
        stringtwo = ""
        i += 1
    return stringone[K-1]



def genThueMorse():
    for n in range("10"):
        return (1 if bin(n).count('1')%2 else 0)
  
  
      
''' 
# ANSWER
one_zero_tree = lambda n, k: bin(2 * k - 1).count('1') % 2



def one_zero_tree(N, K):
    arr= [True]
    j = 2
    flip = False    
    for i in range(1, K):
        if i == j:
            flip = True
            j += j
        if flip:
            arr.append(not arr[i - j / 2])
        else:
            arr.append(not arr[-1])
            
    return 1 if arr[K - 1] else 0




def one_zero_tree(n, k):
    k -= 1
    n = 1
    while k:
        n ^= k
        k /= 2
    return n & 1
