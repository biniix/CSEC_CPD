n = int(input())
cards = list(map(int, input().split()))

s = 0
d = 0
left = 0
right = n -1
turn = 0 

while left <= right:
    if cards[left] > cards[right]:
        pick = cards[left]
        left +=1
    else:
        pick = cards[right]
        right -=1
    if turn == 0:
        s += pick 
    else:
        d +=pick
    turn = 1 - turn
    
print(s,d)
