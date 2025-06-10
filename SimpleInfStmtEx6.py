#SimpleInfStmtEx6.py
n=float(input("Enter a value:"))
if(n>0) and (n%2==0):
    print("{} is Even".format(n))
if(n>0) and (n%2!=0):
    print("{} is odd".format(n))
if(n<0):
    print("{} is invalid Input".format(n))