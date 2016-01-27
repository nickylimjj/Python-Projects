from graph import *

class Puzzle(object):
    """Instance of a puzzle that records it's state (represented as a string) and where the blank is (a string)"""
    def __init__(self, label):
        assert type(label) == str
        for digit in label:
            assert digit in '012345678'
        assert len(label)==9
        self.label = label
        for x in range(len(label)):
            if label[x] == '0':
                self.spot = x
    def makeAMove(self,tile):
        end_state = ''
        for turn in range(len(self.label)):
            if turn == tile:
                end_state+='0'
            elif turn == self.spot:
                end_state+=self.label[tile]
            else:
                end_state+=self.label[turn]
        return Puzzle(end_state)
    def printBoard(self):
        label=self.label
        board=[]
        for i in range(3):
            board.append([label[(3*i)],label[(3*i+1)],label[3*i+2]])
        for e in board:
            print " ".join(e)
        print ''

legal_moves={
    0 :(1,3),
    1 :(0,2,4),
    2 :(1,5),
    3 :(0,4,6),
    4 :(1,3,5,7),
    5 :(2,4,8),
    6 :(3,7),
    7 :(4,6,8),
    8 :(5,7),
}
def notInPath(node, path):
    for elt in path:
        if node.label == elt.label:
            return False
    return True

def BFS(start,end,legal_moves=legal_moves):
    '''
    start: <Puzzle>
    end:<Puzzle>
    remembers path as it goes down
    '''
    initPath = [start]
    queue=[]
    queue.append(initPath)
    steps = 0
    while len(queue) != 0:
        steps +=1
        tmpPath= queue.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label==end.label:
            return (tmpPath,"Completed in {} steps".format(steps))
        for shift in legal_moves[lastNode.spot]:       #creating new nodes and forming edges
            new_child = lastNode.makeAMove(shift)
            if notInPath(new_child,tmpPath):
                new_path=tmpPath+[new_child]
                queue.append(new_path)
        # raw_input("hit enter to continue...\n")
    return None
def printSolution(path,steps):
    for index,e in enumerate(path):
        print 'Move:',index
        e.printBoard()
    print steps

(path,steps) = BFS(Puzzle('123405678'),Puzzle('012345678'))
printSolution(path,steps)
