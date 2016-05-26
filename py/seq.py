def digitDistanceNumber(n):

    result = 0
    lastDigit = n % 10
    tenPower = 1

    n /= 10

    while n:
        result += 
        tenPower *= 10
        lastDigit = n % 10
        n /= 10

    return result

print(digitDistanceNumber(333))
