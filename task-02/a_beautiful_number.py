t=int(input())
for j in range(t):
    s=input()
    c=[0]*10
    for ch in s:
        c[int(ch)]+=1
    r=[]
    for i in range(1,11):
        for d in range(10-i,10):
            if c[d]>0:
                r.append(str(d))
                c[d]-=1
                break
    print("".join(r))
