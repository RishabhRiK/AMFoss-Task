def solve():
    n=int(input())
    x,y=map(int,input().split())
    if n==0:
        print(0)
        return
    if y>=x:
        print((n+x-1)//x)
    else:
        print((n+y-1)//y)

t=int(input())
for j in range(t):
    solve()
