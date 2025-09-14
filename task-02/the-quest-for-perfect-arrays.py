t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    o=[x for x in a if x%2!=0]
    e=[x for x in a if x%2==0]
    
    if e:
        mn_e,mx_e=min(e),max(e)
        c1=sum(1 for x in o if x<mn_e or x>mx_e)
    else:
        c1=n
    
    if o:
        mn_o,mx_o=min(o),max(o)
        c2=sum(1 for x in e if x<mn_o or x>mx_o)
    else:
        c2=n
    
    print(min(c1,c2))