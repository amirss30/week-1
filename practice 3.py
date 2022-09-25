a = int(input('Write 1st number: '))
b = int(input('Write 2nd number: '))
c = int(input('Write 3th number: '))
if a>b:
    if a>c:
        x=a
else:
    if b>b:
        x=b
    else:
        x=c
if a<b:
    if a<c:
        y=a
else:
    if b<c:
        y=b
    else:
        y=c
print('Biggest number is: ' + str(x))
print('Smallest number is: ' + str(y))