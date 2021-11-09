def checkPowlooknong(List, index, pow = 0):
    if (2*index)+1 < len(List):
        pow += List[(2*index)+1]
        checkPowlooknong(List,(2*index)+1,pow)
    if (2*index)+2 < len(List):
        pow += List[(2*index)+2]
        checkPowlooknong(List,(2*index)+2,pow)
    return pow

def checkPow(List, index):
    return int(List[index])+int(checkPowlooknong(List,index))

power,key = input("Enter Input : ").split('/')
Lofpower = [int(i) for i in power.split()]
Lofkey = [i for i in key.split(',')]
sum = 0
for i in Lofpower:
    sum += i
print(sum)
for i in Lofkey:
    a,b = i.split()
    if int(checkPow(Lofpower,int(a))) > int(checkPow(Lofpower,int(b))):
        print(f'{a}>{b}')
    elif int(checkPow(Lofpower,int(a))) == int(checkPow(Lofpower,int(b))):
        print(f'{a}={b}')
    else: print(f'{a}<{b}')