n=int(input())
a=set(map(int, input().split()))
m=int(input())
for _ in range(m):
    action=input()
    if action[0] == "i":
        a.intersection_update(set(map(int, input().split())))
    elif action[0] == "u":
        a.update(set(map(int, input().split())))
    elif action[0] == "s":
        a.symmetric_difference_update(set(map(int, input().split())))
    else:
        a.difference_update(set(map(int, input().split())))
print(sum(a))