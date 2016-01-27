#convert a value (in decimal) to the ans (in binary)

terminal = int(raw_input('terminal value: '))


for i in range(terminal+1):
    value = i                  #refresh all variables
    initialvalue = i
    ans = ''
    
    if value < 0:
        value = abs(value)
        isNeg = True
    elif value == 0:
        ans='0'
        isNeg = False
    else:
        isNeg = False
        
    while value > 0:
        ans= str(value%2)+ans #concatenating string
        value=value/2
        
    if isNeg == True: #conversion
        ans= '-'+ans
    print('In binary form, '+ str(initialvalue) + ' is ' + str(ans))
print('---endofcode---')
    