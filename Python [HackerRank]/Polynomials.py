import numpy

coefs=list(map(float,input().split()))
x=float(input())

print(numpy.polyval(coefs,x))