iter = int(input())

for _ in range(iter):
    alice, x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    
    if alice <= x or alice >= y:
        print("YES")
    else:
        print("NO")
