def createmonthsdic():
    ''' 
    create a dictionary whereby the keys are the numerical assignments and the values are the 3-alphabet associations
    returns: dic
    '''
    
    
    monthsL= 'jan feb mar apr may jun jul aug sep oct nov dec'
    monthsL = monthsL.split(' ')
    i=0
    months=monthsL[:]
    dic={}
    
    #capitalizeing the months
    for month in monthsL:
        month= month.capitalize()
        months[i] = month
        i+=1
        
    #creating dictionary
    for i in range(len(months)):
        dic[i+1]=months[i]
    
    return dic