import math
def fib(nr):
    ratio = (1 + math.sqrt(5)) / 2
    return int(ratio ** nr / math.sqrt(5) + 0.5)
