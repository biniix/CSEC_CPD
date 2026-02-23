a = list(map(int, input().split()))
s = input()

total = 0

for char in s:
    total += a[int(char) - 1]

print(total)
