n = int(input())

home = []
away = []

for _ in range(n):
    h, a = map(int, input().split())
    home.append(h)
    away.append(a)

count = 0

for i in range(n):
    for j in range(n):
        if i != j:
            if home[i] == away[j]:
                count += 1

print(count)
