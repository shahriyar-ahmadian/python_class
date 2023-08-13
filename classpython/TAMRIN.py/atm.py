x=1234
r=0
while r!=3 :
    n=int(input('enter psword:'))
    r+=1
    if n!=x:
        print('psword in nist')
        continue
    elif n==x:
        print('bia to')
        break
