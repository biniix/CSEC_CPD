n = int(input())

magnets = [(input()) for _ in range(n)]

group = 1
for i in range(1, n):
    if magnets[i] != magnets[i - 1]:
        group +=1

print(group)
