#Proghram for accepting a Digit and Display Its Name
#IfElifElseStmtEx1.py
d=int(input("Enter any digit"))
if(d==0):
    print("{} is Zero".format((d)))
elif(d==1):
    print("{} is One".format(d))
elif(d==2):
    print("{} is Two".format((d)))
elif(d==3):
    print("{] is three".format(d))
elif(d==4):
    print("{} is four".format(d))
elif(d==5):
    print("{} is five".format(d))
elif(d==6):
    print("{} is Six".format(d))
elif(d==7):
    print("{} is seven".format(d))
elif(d==8):
    print("{} is Eight ".format(d))
elif(d==9):
    print("{} is Nine ".format(d))
elif(d>9):
    print("{} is +=ve Number".format(d))
elif(d<0) and d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -ve digit".format(d))



