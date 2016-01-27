#MIT solution to find longest string

s='abc' 
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
   
    #compare element with current working string.
    if s[i] >= curString[-1]:
        curString += s[i]
        
        #keep longest string up to date
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest