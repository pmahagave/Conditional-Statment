#program for accepting Value and Decide whether It is Palindrome or Not
#IfEleseStmtEx2.py
value=input("Enter the values:")
if(value==value[::-1]):
    print("'{}' is palindrome".format(value))
else:
    print("'{}' is Not palindrome".format(value))

