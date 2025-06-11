#program for accepting Two Numerical values and Find Biggest
#IfEleseStmtEx1.py
a=float(input("Enter value of a:"))
b=float(int(input("Enter value b")))
if(a>b):
    print("Max({},{})={}".format(a,b,a))
else:
    if(b>a):
      print("Max({},{})={}".format(a,b,b))
    else:
        print("Both values are equal")
    print("I am from inner if else statment")
print("I am from outer if else statment")



