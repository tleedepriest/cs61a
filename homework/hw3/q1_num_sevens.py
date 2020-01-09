def num_sevens(n):
    """Returns the number of times 7 appears as a digit of n.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if n//10 == 0:
        if n%7 == 0:
            return 1
        else:
            return 0
    else:
        if (n%10)%7 == 0:
            return num_sevens(n//10) + 1
        else:
            return num_sevens(n//10)
        
def num_sevens_opt(n):
    """
    Does the same thing as num_sevens
    but is less amount of code
    """
    if n%10 == 7:
        return num_sevens_opt(n//10) + 1
    elif n//10 > 0:
        return num_sevens_opt(n//10)
    else:
        return 0
