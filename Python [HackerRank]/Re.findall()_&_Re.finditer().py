# Enter your code here. Read input from STDIN. Print output to STDOUT

S=input()
vs,cons="[AEIOUaeiou]{2,}","[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]"
import re
res=re.findall(rf"{cons}{vs}(?={cons})",S)  #(?=) is called lookahead assertions

if res:
    for item in res:
        print("".join(re.findall(rf"{vs}",item)))
else:
    print("-1")