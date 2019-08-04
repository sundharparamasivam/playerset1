su=input()
l=list(map(int,input().split()))
l1=[]
for i in l:
    if l.index(i)==i:
        l1.append(i)
if len(l1)==0:
    print(-1)
else:
    l1=sorted(l1)
    for j in l1:
        print(j,end=" ")
