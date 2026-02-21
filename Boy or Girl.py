username = input()

distinct = len(set(username))

if distinct % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
