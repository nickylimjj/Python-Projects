def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    lower = min(a,b)
    higher = max(a,b)
    if lower == 0:
        return higher
    else:
        return gcdRecur(lower,higher%lower)
        
