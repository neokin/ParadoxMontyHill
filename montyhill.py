from random import *
def initABC():
    a=b=c=0
    opr=randint(1, 3)
    if(opr==1):
        a=1
    elif(opr==2):
        b=1
    else:
        c=1

    print(a, b, c)
    return a, b, c

def initD(a, b, c, selectdoor):
    if(a==0 and selectdoor!=1):
        a='n'
    elif(b==0 and selectdoor!=2):
        b = 'n'
    elif(c==0 and selectdoor!=3):
        c = 'n'
    return a, b, c

def getR(a, b, c, selectdoor):
    if((a=='n'and selectdoor==3)or(c=='n'and selectdoor==1)):
        return b
    if((b=='n'and selectdoor==3)or(c=='n'and selectdoor==2)):
        return a
    if((b=='n'and selectdoor==1)or(a=='n'and selectdoor==2)):
        return c



def gameLW():
    selectdoor = randint(1, 3)
    a, b, c = initABC()
    a, b, c = initD(a, b, c, selectdoor)
    rez = getR(a, b, c, selectdoor)
    return rez

wincounter = 0
allcounter = 0
for i in range(100000):
    r = gameLW()
    if(r==1):
        wincounter+=1
    allcounter+=1

print("Процент выигрышей "+str((wincounter/allcounter)*100)+"%")
print("Проведено розыгрышей "+str(allcounter))
print("Из них выиграны "+str(wincounter))
