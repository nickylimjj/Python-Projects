
def printmove(fr,des):
    global count
    count+=1
    print('step '+ str(count)+': '+'move from '+str(fr)+' to '+str(des))
    
def towers(n,fr,des,spare):
    '''
    n: number of rings (integer)
    fr: name of inital location
    des: name of destination
    spare: name of spare ring
    '''
    if n==1:
        printmove(fr,des)
    else:
        towers(n-1,fr,spare,des)
        towers(1,fr,des,spare)
        towers(n-1,spare,des,fr)

def meteredtowers(n,fr,des,spare):
    '''
    n: number of rings (integer)
    fr: name of inital location
    des: name of destination
    spare: name of spare ring
    '''
    global count
    count = 0
    towers(n,fr,des,spare)

meteredtowers(5,'from','to','spare')