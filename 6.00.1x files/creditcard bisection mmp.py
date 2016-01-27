balance = 320000
annualInterestRate = 0.2
low = balance/12
high = (balance*((1+(annualInterestRate/12))**12))/12
mmp = (high+low)/2
epsilon = .005 #correct up to 2dp

def payment(x,y):
    '''
    x: balance
    y: minimum monthly payment
    '''
    for i in range(12):
       unpaid=x-y
       outstanding=unpaid+(annualInterestRate/12)*unpaid
       x=outstanding
    return outstanding

while abs(payment(balance,mmp))>epsilon:
    mmp = (high+low)/2
    if payment(balance,mmp)>0:
        low = mmp
        print('low changed')
    else:
        high = mmp
        print('high changed')
print('Lowest Payment: $'+str(round(mmp,2))+   \
'; outstanding: $'+str(payment(balance,mmp)))

print('balance was: $'+ str(balance)) ,
print('and annual interest rate was: '+str(annualInterestRate*100)+'%')
print('---endofcode---')