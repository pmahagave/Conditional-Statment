#SimpleInfStmtEx7.py
def is_leap(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

    # Write your logic here


x=is_leap(2025)