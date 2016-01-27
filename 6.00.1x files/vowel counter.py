string = 'the quick brown fox jumped over the wall'

vow = ['a','e','i','o','u']
res=0

for char in vow:
    print 'Number of {}\'s: {}'.format(char.upper(),string.count(char))