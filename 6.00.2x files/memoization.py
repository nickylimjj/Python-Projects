def fib(x,memo={}):
    if x <2:
        return x
    if x in memo:
        return memo[x]
    results = fib(x-1,memo)+fib(x-2,memo)
    memo[x]=results
    return results

for i,index in enumerate(range(51)):
    print 'Fib number {}: {}'.format(index,fib(i))