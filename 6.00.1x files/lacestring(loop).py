def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """  
    res = ''
    excess=''
    if len(s1)>len(s2):
        excess = s1[len(s2):]
        s1=s1[:len(s2)]
        
    if len(s2)>len(s1):
        excess = s2[len(s1):]
        s2=s2[:len(s1)]
        
    if len(s1)==len(s2):
        for i in range(len(s1)):
            res+=s1[i]+s2[i]
    
        return res+excess