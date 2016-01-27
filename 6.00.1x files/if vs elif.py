print('this code prints ALPHA when <3, BRAVO when <5, \
YANKEE when <7, ZULU when <9 \
skips all when >=9')


end = int(raw_input('input terminal integer: '))
count = 0
for x in range(end+1):
    count=x
    print('for value x = '+ str(count))
    if x<3:
        print ('ALPHA')
    if x<5:
        print ('BRAVO')    
    elif x<7:
        print ('YANKEE')
        print ('only reached when both if test BEFORE are False')
        print ('does not consider subsequent elif')
    elif x<9:
        print ('ZULU')
    if x<10:
        print('CHARLIE')
    else:
        print('All tests were False')    
print('')
print('---endofcode---')