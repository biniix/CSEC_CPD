s = input().strip()

current_position = 0 
total_moves = 0

for char in s:
    target_postion = ord(char) - ord("a")
    diff = abs(current_position - target_postion)
    moves = min(diff,26 - diff)
    
    total_moves +=moves
    current_position = target_postion
    
print(total_moves)
