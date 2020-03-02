HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def num_sevens(n):
    """Returns the number of times 7 appears as a digit of x.

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
        if n%7 == 0 and n!=0:
            return 1
        else:
            return 0
    else:
        k = n%10
        if k%7 == 0 and k!=0:
            return num_sevens(n//10) + 1
        else:
            return num_sevens(n//10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """ 
    def ping_pong_plus(n, index, count):
        if n == index:
            return count
        else:
            if index==0:
                return ping_pong_plus(n, index+1, count+1) # initialize the count 
            elif num_sevens(index+1)!= 0 or (index+1)%7 == 0:
                return ping_pong_minus(n, index+1, count+1)
            else:
                return ping_pong_plus(n, index+1, count+1)
    
    def ping_pong_minus(n,index, count):
        if n == index:
            return count
        else:
            if num_sevens(index+1)!= 0 or (index+1)%7 == 0:
                return ping_pong_plus(n, index+1, count-1)
            else:
                return ping_pong_minus(n, index+1, count-1)
    
    return ping_pong_plus(n, 0, 0)

def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    def find_max_power(total):
        """returns the power to raise the value of 2 for a given total"""
        if total < 2:
            return 0
        else:
            return find_max_power(total/2) + 1

    def count_partitions(n, m):
        """Count the ways to partition n using parts up to m."""
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m < 1:
            return 0
        else:
            return count_partitions(n-m, m) + count_partitions(n, m-(m/2))
   #n=7 , m = 4
   #count_partitions(3,4) + count_partitions(7, 2)
   #count_partitions(-1, 4) + count_partitions(3,2)+count_partitions(5,2)+count_particionas(7,1)
   #0 + c_p(1,2)+c_p(3,1)
   # the issue is that m-m/2 will never go to zero....so the function will never end...below 1?
   #yes!!! I did it!!

    max_power = find_max_power(total)
    max_coin = 2**max_power
    return count_partitions(total, max_coin)

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    if n//10 == 0: #we are at the last digit
        return 0
    elif (n//10)%10 == n%10:
        return missing_digits(n//10) + 0
    elif (n//10)%10 == n%10 - 1:
        return missing_digits(n//10) + 0
    else:
        return missing_digits(n//10) + ((n%10)-1)-((n//10)%10)
    #1248//10 == 124
    #1248 % 10 = 8
    #124 + 8-()

    return missing_digits_helper(n, n%10)
###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
