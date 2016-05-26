dictionary = {}

temp = [int(x) for x in input().split()]
N = temp[0]
S = temp[1]
M = temp[2]

modVal = 1000000009

for i in range(S):
    tempory = [int(x) for x in input().split()]
    dictionary[i + 1] = tempory[1:]

mainArray = [0 for i in range(N)]


def func1(set_number, t):
    set_list = dictionary[set_number]
    for i in set_list:
        mainArray[i - 1] += t


def func2(set_number):
    set_list = dictionary[set_number]
    tot = 0
    for i in set_list:
        tot += mainArray[i - 1]
    print(tot % modVal)


def func3(l, r, t):
    for i in range(l - 1, r):
        mainArray[i] += t


def func4(l, r):
    tot = 0
    for i in range(l - 1, r):
        tot += mainArray[i]
    print(tot % modVal)


for j in range(M):
    init = [int(x) for x in input().split()]

    selector = init[0]

    if selector == 1:
        func1(init[1], init[2])
    elif selector == 2:
        func2(init[1])
    elif selector == 3:
        func3(init[1], init[2], init[3])
    elif selector == 4:
        func4(init[1], init[2])
