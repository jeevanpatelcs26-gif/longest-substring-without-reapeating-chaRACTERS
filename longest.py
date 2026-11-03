
s="abcabcbb"

def length(s):
    l, best = 0, 0
    seen = {}
    for r, i in enumerate(s):
        if i in seen and seen[i] >= l:
            l = seen[i] + 1
        seen[i] = r
        best = max(best, r - l + 1)
    return best
print(length(s))


