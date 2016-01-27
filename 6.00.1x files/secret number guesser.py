
low = 0
high = 100

print('Please think of a number between 0 and 100!')
while True:
    ans = (high+low)/2
    print('Is your secret number '+str((high+low)/2)+'?')
    print("Enter 'h' to indicate the guess is too high."),
    print("Enter 'l' to indicate the guess is too low."),
    print("Enter 'c' to indicate I guessed correctly."),
    resp = str(raw_input())
    if resp == 'h':
        high=ans
    elif resp == 'l':
        low=ans
    elif resp == 'c':
        ans = str((high+low)/2)
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: '+str(ans))