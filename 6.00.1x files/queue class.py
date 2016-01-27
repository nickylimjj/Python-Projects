class Queue(object):
    '''new type which creates a queue'''
    
    def __init__(self):
        self.vals = []
    def ins(self,e):
        '''inserts element, e into the queue'''
        self.vals.append(e)
    def remove(self):
        '''pops first element out of the queue. If list is empty, raises a ValueError'''
        if self.vals == []:
            raise ValueError()
        else:
            return self.vals.pop(0)
    def __str__(self):
        return str(self.vals)

q=Queue()
q.ins(1)
q.remove()
print q