#program for accepting Value and Decide whether It is Palindrome or Not
#SimpleInfStmtEx4.py
value=input("Enter the value:")
if(value==value[::-1]):
    print("'{}' is palindrome".format(value))
if(value!=value[::-1]):
    print("'{}' is not palindrome".format(value))

