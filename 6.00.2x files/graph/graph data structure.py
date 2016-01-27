class Node(object):
    """
    Node: creates a node
    inputs:name (str)
    """
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __repr__(self):
        return "{}".format(self.name)

class Edge(object):
    """
    Edge: creates an edge
    inputs: src (Node object), dest (Node object)
    """
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __repr__(self):
        return "{} -> {}" .format(self.src,self.dest)

class WeightedEdge(Edge):
    """
    WeightedEdge: an edge with assigned weight (default to 1)
    input: src (Node object), dest (Node object), weight = 1.0 (int/float)
    """
    def __init__(self, src,dest, weight = 1.0):
        # super(WeightedEdge,self).__init__(src,dest)   #either is fine
        Edge.__init__(self,src,dest)                    #either is fine
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __repr__(self):
        return "{} -({})-> {}" .format(self.src,self.weight,self.dest)
        

class Digraph(object):
    """
    Digraph: collection of nodes and edges (an adjacency dictionary. ie, n1: [n2,n3]
    """
    def __init__(self):
        self.nodes = set([])
        self.edges = {}

    def getNode(self,node): #node (str)
        for elem in self.nodes:
            if node == elem:
                return elem
        else:
            raise ValueError('node not found')
    def getNodes(self):
        return self.nodes
    def getAdjDic(self):
        return self.edges
    def addNode(self,node):
        if node in self.nodes:
            raise ValueError('duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node]=[] #initialize an empty list for destinations
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('node not found')
        self.edges[src].append(dest)
    def getChildren(self,node):
        return self.edges[node]
    def __str__(self):
        res='graph\n'+''
        for node in self.edges:
            for dest in self.edges[node]:
                res='{0}{1}->{2}\n'.format(res,node,dest)
        return res

class Graph(Digraph):
    """
    Graph: a collection of nodes and bidirectional edges
    inputs: None
    """
    def __init__(self):
        super(Graph, self).__init__()
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev =Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self,rev)
    def addEdge_oneway(self,edge):
        # super(Graph,self).addEdge(edge)   #either is fine
        Digraph.addEdge(self,edge)          #either is fine

def createNodes(numnodes,graphtype):
    '''
    createNodes: build a digraph with input number of nodes
    inputs: numnodes (integer), graphtype (Graph() or Digraph())
    '''
    nodes = []
    for n in range(1,numnodes+1):
        nodes.append('n{}'.format(str(n)))
    g = graphtype()
    for n in nodes:
        g.addNode(n)
    return g

digraph1 = createNodes(4,Digraph)
n1_n2 = WeightedEdge(digraph1.getNode('n1'),digraph1.getNode("n2"))
n1_n3 = WeightedEdge(digraph1.getNode('n1'),digraph1.getNode("n3"))
n2_n4 = WeightedEdge(digraph1.getNode('n2'),digraph1.getNode("n4"))
n4_n1 = WeightedEdge(digraph1.getNode('n4'),digraph1.getNode("n1"))
digraph1.addEdge(n1_n2)
digraph1.addEdge(n1_n3)
digraph1.addEdge(n2_n4)
digraph1.addEdge(n4_n1)

digraph2 = createNodes(7,Digraph)
n1_n2 = WeightedEdge(digraph2.getNode('n1'),digraph2.getNode("n2"))
n1_n3 = WeightedEdge(digraph2.getNode('n1'),digraph2.getNode("n3"))
n2_n5 = WeightedEdge(digraph2.getNode('n2'),digraph2.getNode("n5"))
n3_n3 = WeightedEdge(digraph2.getNode('n3'),digraph2.getNode("n4"))
n4_n1 = WeightedEdge(digraph2.getNode('n4'),digraph2.getNode("n1"))
n4_n6 = WeightedEdge(digraph2.getNode('n4'),digraph2.getNode("n6"))
n4_n7 = WeightedEdge(digraph2.getNode('n4'),digraph2.getNode("n7"))
n5_n4 = WeightedEdge(digraph2.getNode('n5'),digraph2.getNode("n4"))
n5_n6 = WeightedEdge(digraph2.getNode('n5'),digraph2.getNode("n6"))
n6_n7 = WeightedEdge(digraph2.getNode('n6'),digraph2.getNode("n7"))
digraph2.addEdge(n1_n2)
digraph2.addEdge(n1_n3)
digraph2.addEdge(n2_n5)
digraph2.addEdge(n3_n3)
digraph2.addEdge(n4_n1)
digraph2.addEdge(n4_n6)
digraph2.addEdge(n4_n7)
digraph2.addEdge(n5_n4)
digraph2.addEdge(n5_n6)
digraph2.addEdge(n6_n7)

print digraph1
print digraph2
#recursive program
def DFS_recursive(graph,start,end,path=[],shortest=None): #path is to keep track of where it's been
    '''
    DFS: Find a path form start to end by recursive means. Assumes Digraph
    input: graph (digraph object), start and end, (node object), path (list)
    '''
    path = path + [start]
    print 'Currently at path:{}' .format(path)

    if start == end: #base case
        return path
    for node in graph.getChildren(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest): #if path not found or a shorter path is found
                newpath = DFS(graph,node,end,path,shortest)
                if newpath != None: #if a path is found, update shortest to be the path found
                    shortest = newpath
    return shortest

def DFS(graph,start,end): #has to run through entire tree
    stack = []
    shortest = None
    initPath = [start]
    stack.append(initPath)
    while len(stack) != 0:
        tempPath = stack.pop(0)
        lastNode = tempPath[len(tempPath)-1]
        print 'current at: {}' .format(tempPath)
        if lastNode == end:
            if shortest == None or len(tempPath)<len(shortest):
                print 'solution found'
                shortest = tempPath
        for linkNode in reversed(graph.getChildren(lastNode)):
            if linkNode not in tempPath:
                newPath = tempPath+[linkNode]
                stack.insert(0,newPath)
    return shortest

def BFS(graph,start,end):
    queue=[]
    initPath = [start]
    queue.append(initPath)
    while len(queue) != 0:
        tempPath= queue.pop(0)
        lastNode = tempPath[len(tempPath)-1]
        print 'Popped path: {}'.format(tempPath)
        if lastNode == end:
            return tempPath
        for linkNode in graph.getChildren(lastNode):
            newPath = tempPath+[linkNode]
            queue.append(newPath)

    return None
print "\n\n DFS: \n\n"
x = DFS(digraph2,digraph2.getNode('n1'),digraph2.getNode("n7"))
print 'shortest path:',x
print '\n\n BFS: \n\n'
x = BFS(digraph2,digraph2.getNode('n1'),digraph2.getNode("n7"))
print x