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

if __name__ == "__main__":
