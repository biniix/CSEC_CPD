n = int(input())
impl = 0

for _ in range(n):
    p,v,t = map(int, input().split())
    if p+v+t>=2:
        impl+=1

print(impl)
