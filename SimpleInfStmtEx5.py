#Prohram for accepting a value and Decide weather It is +Ve OR 0-ve or 0
#SimpleInfStmtEx5.py

try:
    n = int(input("Enter a value:"))
    if(n>0):
        print("\t{} is +ve".format(n))

    if(n<0):
        print("\t{} is -ve".format(n))

        print("")
    if(n==0):
        print("\t{} is zero".format(n))
except ValueError:
    print("Character is Invalid")