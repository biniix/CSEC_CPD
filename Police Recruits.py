n = int(input())
events = list(map(int, input().split()))

free_police = 0
untreated_crime = 0

for event in events:
    if event > 0:
        free_police += event
    else:
        if free_police > 0:
            free_police -= 1
        else:
            untreated_crime +=1
        
print(untreated_crime)
