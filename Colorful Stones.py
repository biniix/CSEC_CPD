s = input()
t = input()

pos = 0
for c in t:
    if s[pos] == c:
        pos += 1

print(pos + 1)
