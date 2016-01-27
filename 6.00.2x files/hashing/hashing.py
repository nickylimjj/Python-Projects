class Hash(object):
    def __init__(self,numBuckets=20):
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self,key,value):
        hashbucket = self.buckets[key%self.numBuckets]
        #if entry exists
        for index in range(len(hashbucket)):
            if hashbucket[index][0] == key:
                hashbucket[index] = (key,value)
        #else,
        hashbucket.append((key,value))

    def getEntry(self,key):
        hashbucket = self.buckets[key%self.numBuckets]
        for index in range(len(hashbucket)):
            if hashbucket[index][0] == key:
                return hashbucket[index][1]

    def __repr__(self):
        return 'There are {} buckets' .format(self.numBuckets)


import random
random.seed(0) #create one instance in stochastic model


def sim(hash,runs=50):
    for value in range(runs):
        key = random.randint(0,10**5)
        hash.addEntry(key,value)
#printing the bucket composition
def prtsim(hash):
    print hash
    for count, hashbucket in enumerate(hash.buckets):
        numElements = len(hashbucket)
        print "No {}:" .format(count+1), hashbucket, '---{} items---' .format(numElements)



hash = Hash()
sim(hash)
prtsim(hash)

# apple = Hash(25)
# sim(apple)
# prtsim(apple)





