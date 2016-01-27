#convert a value (in decimal) to the ans (in binary)

value = int(raw_input('value: '))
initialvalue = value
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
    