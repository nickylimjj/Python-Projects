#bob counting program

s='abobasdadbobobs'

bobcount=0

for x in range(len(s)):
    if s[x:x+3] == 'bob':
        bobcount+=1
print('Number of times bob occurs is: '+str(bobcount))