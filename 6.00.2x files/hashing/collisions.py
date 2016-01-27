def collision_prob(numBuckets, numInsertions):
    '''
    Given the number of buckets and the number of items to insert, 
    calculates the probability of a collision.
    '''
    prob = 1.0
    for i in range(1, numInsertions):
        prob = prob * ((numBuckets - i) / float(numBuckets))
    return 1 - prob

# def maxInsertion(numBuckets=365,prob = 0.99):
#     '''
#     Given the number of buckets and the probability limit,
#     calculate the maximum number of Insertions
#     '''

#     ans = numBuckets
#     while collision_prob(numBuckets,ans) >= 0.99:
#         ans -= 1


#     return ans

def maxInsertion(numBuckets=365,prob = 0.99, epsilon = 0.005):
    '''
    Given the number of buckets and the probability limit,
    calculate the maximum number of Insertions
    '''

    high = numBuckets
    low = 0
    ans = (high+low)/2
    print 'accepts {} to {}' .format(prob-epsilon,prob+epsilon)

    while abs(collision_prob(numBuckets,ans)-prob) > epsilon:

        if collision_prob(numBuckets,ans) > prob:
            high = ans
            print 'collision_prob({}) = {} ==> too high' .format(ans,collision_prob(numBuckets,ans))
        if collision_prob(numBuckets, ans) < prob:
            low = ans
            print 'collision_prob({}) = {} ==> too low' .format(ans,collision_prob(numBuckets,ans))
        
        ans = (high+low)/2

    return ans