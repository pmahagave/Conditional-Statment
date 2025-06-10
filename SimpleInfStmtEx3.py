#program for accepting Two Numerical values and Find Biggest
# and Check for Equality.
#SimpleInfStmtEx3.py
a=float(input("Enter Value of a:"))
b=float(input("Enter value of b:"))
if(a>b):
    print("Max({},{})={}".format(a,b,a))
if(b>a):
    print("Max({},{})={}.".format(a,b,b))
if(a==b):
    print("Both Values are Equals")
print("Program Execution Completed")