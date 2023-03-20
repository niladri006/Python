# Enter your code here. Read input from STDIN. Print output to STDOUT

int(input())
N = input().split()
Nint = set(list(map(int, N)))
int(input())
M = input().split()
Mint = set(list(map(int, M)))
res = []
for i in list(Nint.difference(Mint)):
    res.append(i)
for j in list(Mint.difference(Nint)):
    res.append(j)
for k in sorted(res):
    print(k)
