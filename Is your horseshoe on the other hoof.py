s1, s2, s3, s4 = map(int, input().split())
unique_colors = len({s1, s2, s3, s4})
to_buy = 4 - unique_colors
print(to_buy)
