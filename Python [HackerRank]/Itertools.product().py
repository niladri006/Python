# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product
A = input().split()
A = list(map(int,A))
B = input().split()
B = list(map(int, B))
output = list(product(A,B))
for i in output:
    print(i, end = " ");