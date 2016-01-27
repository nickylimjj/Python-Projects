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