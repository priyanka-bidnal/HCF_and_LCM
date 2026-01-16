import sys
if len(sys.argv)==3:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    print("User provided")
else:
    a=12
    b=18
    print("No user provided")
    print("HCF and LCM of two numbers")
def hcf(a,b):
    while a:
        a,b=b,a%b
        return a
h=hcf(a,b)
l=(a*b)//h
print("HCF=",h)
print("LCM=",l)        
