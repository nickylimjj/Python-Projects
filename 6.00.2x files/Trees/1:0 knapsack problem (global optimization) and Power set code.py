class item(object):

    def __init__(self, name, value, price):
        self.name = name
        self.value = value
        self.price = price
    def getname(self):
        return self.name
    def getvalue(self):
        return self.value
    def getprice(self):
        return self.price
    def __repr__(self):
        return'<{},value: ${},price: ${}>' . format(self.name,self.value,self.price)



def builditem():
    name = ['radio','underwear','pillow','dog','cat']
    value = [29,2,10,100,50]
    price = [50,7,15,300,300]
    items = []
    for i in range(len(value)):
        items.append(item(name[i],value[i],price[i]))
    return items

items = builditem() #list of item-objects

def value(item):
    return item.getvalue()

def price(item): 
    return item.getprice()

# def f(items,fcn):
#     return sorted(items,key=fcn, reverse = False)  #key: a function that associates a comparison key for each list element and defines an ordering

# # print f(items,value)

def DtoB(num,digit_length):
    
    assert 2**digit_length > num
    bstr = ''

    while num>0:
        bstr = str(num%2) + bstr
        num = num//2 #floor division

    while digit_length - len(bstr) > 0:
        bstr = '0'+bstr
    return bstr

def genPset(items):
    '''
    examines items (a list) and generate all possible binaries to describe subsets.
    Finally, convert binaries back into item subsets (a power set)
    returns: power subset (list)
    '''
    Pset = []
    template = []
    for i in range(2**len(items)):
        template.append(DtoB(i,len(items)))

    for t in template:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(items[j])
        Pset.append(elem)
    
    return Pset

def choosebest(Pset,constraint):
    '''
    inspect each combination in pset individually.
    King of the hill style: each combination stays as the 'best' until a better one is found
    returns: combination, best_val, price
    '''
    best_val = 0.0
    price = 0.0
    Combination = None

    for combination in Pset:
        combination_val = 0.0
        combination_price  = 0.0
        for item in combination:
            combination_val += item.getvalue()
            combination_price += item.getprice()

        if combination_price <= constraint and combination_val>best_val:
            best_val = combination_val
            price = combination_price
            Combination = combination

    return Combination, best_val, price

def test():
    '''
    Initialize a list of items and generate all combinations (power set)
    Returns: best result by 0/1 knapsack problem
    '''
    items = builditem()
    pset = genPset(items)
    combi, val, price = choosebest(pset, 100)
    print "best combination: \n {} \n value: ${} \n price: ${}" .format(combi,val,price)

test()
