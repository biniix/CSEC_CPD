import math
y, w = map(int, input().split())
m = max(y, w)
a = 7 - m
b = 6
g = math.gcd(a, b)
print(a // g, "/", b // g, sep="")
