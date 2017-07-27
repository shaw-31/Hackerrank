arr=[]
s=0
sums=[]
for i in range(6):
    a1 = [int(x) for x in input().strip().split(' ')]
    arr.append(a1)
for i in range(0,4):
    for j in range(0,4):
        for k in range(j,j+3):
            s=s+arr[i][k]+arr[i+2][k]
        mid=(j+(j+2))//2
        s=s+arr[i+1][mid]
        sums.append(s)
        s=0
print(max(sums))



