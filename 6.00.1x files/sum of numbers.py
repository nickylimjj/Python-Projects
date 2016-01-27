end = int(raw_input('enter terminal number: '))
ans = 0

for x in range(1,end+1):
     ans+=x #stacking the answer
     print'iteration no.',str(x),':',str(ans)
print('---endofcode---')