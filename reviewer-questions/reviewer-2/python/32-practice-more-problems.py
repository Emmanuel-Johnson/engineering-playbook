s = "abcabcbb"

seen = set()
res = 0
j = 0

for i in range(len(s)):

    if s[i] in seen:

        while s[j] != s[i]:
            seen.remove(s[j])
            j += 1

        j += 1

    else:
        seen.add(s[i])

    res = max(res, i - j + 1)

print(res)