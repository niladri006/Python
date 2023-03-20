n=int(input("ENTER A NUMBER: "))
count=0
i=1
while(i<=n):
   j=1
   while(j<=i):
       if(i%j==0):
           count=count+1
           j=j+1
       if(count==2):
           print("PRIME NUMBER:-",i)           
   i=i+1
