su=input()
l=list(map(int,input().split()))
l1=[]
f=-1
for i in l:
    f+=1
    if f%2==0 and i%2!=0:
        l1.append(i)
    elif (f%2!=0 and i%2==0):
        l1.append(i)
for j in l1:
    print(j,end=" ")
