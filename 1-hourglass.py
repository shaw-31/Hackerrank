'''
Sample Input:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output:
19
Explanation:
The following hourglasses are:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum (19) is:
2 4 4
  2
1 2 4
'''

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



