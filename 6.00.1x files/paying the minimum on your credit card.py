#paying the minimum on your credit card

monthlyPaymentRate = 0.04
balance = 4213
annualInterestRate = 0.2

MIR= (annualInterestRate) / 12.0 #monthly interest rate


for i in range(1,13):
    mmp = monthlyPaymentRate * balance
    mub = balance - mmp #minimum unpaid balance
    balance = (1+MIR)*mub #balance after including compounding interest
    print 'Month:',i
    print 'Minimum monthly payment:', ('$'+str(round(mmp,2)))
    print 'Remaining balance:', ('$'+str(round(balance,2)))