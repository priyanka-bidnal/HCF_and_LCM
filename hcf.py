import sys
import math
if len(sys.argv)==3:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    print("User provided")
else:
    a=12
    b=18
    print("No user provided")
    print("HCF and LCM of two numbers")
h=math.gcd(a,b)
l=(a*b)//h
print("HCF=",h)
print("LCM=",l)        
