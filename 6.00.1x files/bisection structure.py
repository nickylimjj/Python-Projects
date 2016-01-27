def f(x,epsilon = 0.5):
    high = x
    low = 0
    ans = (high+low)/float(2)
    f_inverse = ans**2

    while abs(f_inverse-x) >epsilon:
        if f_inverse > x: #too high
            high = ans

        else:
            low = ans
        ans = (high+low)/float(2)
        f_inverse = ans**2
        
        
    return round(ans,2)
