import pylab

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 15
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5
#set size of markers
pylab.rcParams['lines.markersize'] = 10

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def bin(n,r,p):
    res = nCr(n,r)*(p**(n-r))*(1-p)**r
    return res


y = []
for i in range(0,50):
    y.append(round(bin(50,i,0.5),3))

pylab.plot(y, 'r', label = 'binomial dist') #r refers to red
pylab.title('binomial graph')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.legend(loc='best')
pylab.show()
print x, y