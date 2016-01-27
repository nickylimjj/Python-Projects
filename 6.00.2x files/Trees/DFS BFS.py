import pylab
import random

class Node(object):
    '''
    Create a binary tree with attributes: Value, Parent, Children (max 2)
    '''
    def __init__(self,v):
        self.value = v
        self.parent = None
        self.left = None
        self.right = None
    
    def getValue(self):
        return self.value
    def getParent(self):
        return self.parent
    def getLeftBranch(self):
        return self.left
    def getRightBranch(self):
        return self.right
    def setParent(self,parent):
        self.parent = parent
    def setLeftBranch(self,left):
        self.left = left
    def setRightBranch(self,right):
        self.right = right
    def isleaf(self):
        return self.left == None and self.right == None
    def __repr__(self):
        return "Value: {}" .format(self.value) 
    

n5 = Node(5)
n2 = Node(2)
n8 = Node(8)
n1 = Node(1)
n4 = Node(4)
n6 = Node(6)
n3 = Node(3)
n7 = Node(7)


n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n4.setLeftBranch(n3)
n3.setParent(n4)
n6.setRightBranch(n7)
n7.setParent(n6)


def DFS(root,fcn):
    '''
    returns boolean 
    depth first search (last-in-first-out LIFO). initializes a stack to determine search.
    returns: node where fcn is true

    root: a Node object
    fcn: a function that returns T/F

    returns: T/F
    '''
    stack = [root]
    while len(stack) > 0:
        print 'at node',stack[0].getValue()    #at top of stack
        if fcn(stack[0]):
            return True

        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch())
            
    return False

def BFS(root,fcn):
    '''
    breath first search (first-in-first-out FIFO). Look at all parents before children (by appending it to the back)
    root: a Node object
    fcn: a function that returns T/F

    returns: T/F
    '''
    queue = [root]
    while len(queue)>0:
        print 'at node',queue[0].getValue()

        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getLeftBranch():                   #if it's not None, it passes
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
    return False


def find6(node):
    return node.getValue() == 6



def BuildDTree(bag,table):
    '''
    builds a decision tree where left = with item and right = without item.

    bag: list of items taken
    table: list of items to be considered. If empty, it's a leaf in the decision tree.

    returns: parent, setting L and R
    '''
    if len(table)== 0:   #a leaf in the tree. Base case
        return Node(bag)
        
    withitem = BuildDTree(bag+[table[0]],table[1:])
    withoutitem = BuildDTree(bag,table[1:])
    parent = Node(bag)
    parent.setLeftBranch(withitem)
    parent.setRightBranch(withoutitem)
    return parent





def printTree(root):
    '''
    prints all nodes in  binary decision tree EXCEPT root node.
    '''
    global node_number 

    if root.isleaf():
        pass
    else:
        L = root.getLeftBranch()
        R = root.getRightBranch()
        node_number += 1
        print node_number, L
        node_number += 1
        print node_number, R

        printTree(L)
        printTree(R)

def sumofDtree(x):
    if x==1:
        return 1
    return x+sumofDtree(x/2)


def numnodes(root,bag,table):
    '''
    returns a graph of number of nodes against number of items on table

    root: the start of a decision tree

    return: 
    '''
    xVals = [x for x in range(len(table)+1)]
    yVals = []

    for x in xVals:
        yVals.append(sumofDtree(2**x)+1)

    pylab.semilogy()
    pylab.plot(xVals,yVals,'ro')
    pylab.title('number of nodes against number of items on the table')
    pylab.xlabel('number of items on the table')
    pylab.ylabel('number of nodes')
    pylab.show()

        
print 'DFS vs BFS'
print 'DFS:'
print DFS(n5,find6)
print 'BFS:'
print BFS(n5,find6)

# node_number = 1
# print 'Decision tree'
# bag = []
# table = ['chocolate','pen','puppy','phone','bookmark']
# print "bag: "+str(bag)
# print "table: " +str(table)
# root = BuildDTree(bag,table) #build tree
# print '\n\n\nTree nodes below: \n\n\n'
# printTree(root)
# numnodes(root,bag,table)
