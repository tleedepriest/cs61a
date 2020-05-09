"""
cs61a Spring 2020 Discussion Tree Recursion and Lists
"""

def count_stair_ways(n):
    """
    Parameters
    -----------
    n: int
        whole number of stairs

    Returns
    ----------
    if you are allowed to go up the stairs with
    either one or two steps, count the number
    of ways you can climb the steps
    """
    if n == 1 or n == 0:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n, k):
    """
    Parameters
    -----------
    n: int
        whole number of stairs
    k: int
        the biggest step you can take up the stairs

    Returns
    ----------
    The number of ways you can go up a set of stairs n
    if the biggest step you can take is k steps
    and you are allowed to take any number of 
    steps up to and including k steps
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif k == 0:
        return 0
    else:
        i = 1
        total = 0
        while i <= k:
            total += count_k(n-i, k)
            i += 1
        return total
def wwpd():
    """
    perform a series of operations
    and guess what python would
    display
    """
    a = [1, 5, 4, [2, 3], 3]

    #1 3 
    print("I think it displays 1 3,"\
          "it actually displays")
    print(a[0], a[-1])

    print("I think it displays 5,"\
          "it actually displays {}".format(len(a)))
    
    
    print("I think it displays False,"\
          "it actually displays {}".format(2 in a))
    
    print("I think it displays True,"\
          "it actually displays {}".format(4 in a))
    
    print("I think it displays 2,"\
          "it actually displays {}".format(a[3][0]))

def even_weighted(s):
    """
    This function takes the elements in the input list
    and returns even indexed elements multiplied by
    the value of their index using a list
    comprehension
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [x*s.index(x) for x in s[::2]]

def even_weighted_v2(s):
    """
    This function takes the elements in the input list
    and returns even indexed elements multiplied by
    the value of their index using a list
    comprehension
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i*s[i] for i in range(len(s)) if i%2==0]

def max_product(s):
    """Return the maximum product 
    that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not s:
        return 1
    else:
        return max(max_product(s[1:]), s[0]*max_product(s[2:]))

def check_hole_number(n):
    """
    A hole numberis a number in which every other digit dips 
    below the digits immediately adjacent to it
    function only accepts numbers with odd number of digits
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    #define variables because my working memory is bad
    end_digit = n%10
    remaining = n//10
    adjacent_end = (n//10)%10
    adjacent_adjacent_end = (n//100)%10

    if adjacent_end < end_digit and adjacent_end < adjacent_adjacent_end:
        return check_hole_number(n//100) #every OTHER digit
    #if it itterates through everything then then n will be one digit
    return not n//10

def check_mountain_number(n):
    """
    (b) Define the following function so that it properly 
    identifies mountain numbers. A mountain number is a
    number that either
    
    i. 
    
    has digits that strictly
    
    decrease from right to left OR 
    
    strictly
    
    increase from right to left
    
    ii. has digits that increase from right to left up to some 
    point in the middle of the number 
    (not necessarily the exact middle digit).

    After reaching the maximum digit, the digits to the left 
    of the maximum digit should strictly decrease.

    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper(n, is_increasing_l_to_r):
        """
        helper function to determine if mountain number
        """
        last_dig = n%10
        adj_last = (n//10)%10

        if n//10 == 0:
            return True # arbitrary value

        if last_dig < adj_last and is_increasing_l_to_r:
            return helper(n//10, True) 
        return last_dig > adj_last and helper(n//10, False) 

    return helper(n, is_increasing_l_to_r=True)
    
 
if __name__ == "__main__":
    wwpd()
    print(even_weighted([1,2,3,4,5,6]))
    print(max_product([3,5,7,8,3,2,78,5,9,-2,-9,-90]))

    print(check_hole_number(123))
    print(check_hole_number(3241968))
    print(check_hole_number(3245968))

    print(check_mountain_number(103))
    print(check_mountain_number(153))
    print(check_mountain_number(123456)) 
