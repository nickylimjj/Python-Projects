testbit = 0b10001011

for i in range(testbit.bit_length()):
    bitmask = 2**i #a number
    if testbit & bitmask > 0:
        print '{}th bit is on'.format(i+1)