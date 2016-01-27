import pylab
import random

#A gaussian pdf
def normal(mean,sd,numSamples):
    samples = []
    for i in xrange(numSamples):
        samples.append(random.gauss(mean,sd)) 

    pylab.hist(samples,bins=100)  

pylab.title('gaussian pdf')
pylab.ylabel('no. of occurence')
pylab.xlabel('value')

normal(0.0,1,100000)
pylab.show()
b