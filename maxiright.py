su=input()
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)):
    if l[i]==max(l[i:]):
        l1.append(l[i])
print(*l1)
print(max(l1))
