def PlayWithStringsIII(S, k):
    i = j = K = 0
    res = (0,0)
    last = {}

    while i < len(S):
        if K == k and j - i > res[1] - res[0]:
            res = (i,j)

        if K <= k and j + 1 <= len(S):
            if not last.has_key(S[j]):
                K = K + 1
            last[S[j]] = j
            j = j + 1
        else:
            if last[S[i]] == i:
                del last[S[i]]
                K = K - 1
            i = i + 1
    return S[res[0]:res[1]]

print(PlayWithStringsIII("abcbaa",3))
