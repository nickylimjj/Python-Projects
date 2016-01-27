class item(object):
    """an item with a name, weight and value"""
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
    def getName(self):
        return self.name
    def getWeight(self):
        return self.weight
    def getValue(self):
        return self.value
    def getDensity(self):
        return float(self.value)/float(self.weight)
    def __repr__(self):
        return '<{},weight: {}kg,value: ${}, density: {}>' .format(self.name,self.weight,self.value,self.getDensity())

def buildItems():
    result=[]
    names = ['biscuits','pen','laptop','wine','book','candle lamp','newspapers']
    weights = [.26,.05,1.6,.75,.2,.2,.7]
    values = [4.0,1.9,1670.0,30.0,4.0,39.0,2.0]
    for i in range(len(names)):
        result.append(item(names[i],weights[i],values[i]))
    return result

def getValue(item):
    return item.getValue()

def getDensity(item):
    return item.getDensity()

def greedyAlgorithm(items,constraint,fcn=getDensity):
    result = []
    items = sorted(items,key=fcn,reverse=True) #most valuable in front
    while constraint > 0 and len(items)>0:
        temp = items.pop(0)
        if temp.getWeight() <= constraint:
            result.append(temp)
            
        constraint -= temp.getWeight()

    return result
    


def testgreedy():
    items = buildItems()
    constraint = 3.5
    fcn = getDensity
    result = greedyAlgorithm(items,constraint,fcn)
    if len(result) == len(items):
        print 'take everything'
    else:
        for item in result:
            print item


testgreedy()
