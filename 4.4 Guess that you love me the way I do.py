class Queue:
    def __init__(self):
        self.items =[]
    def enQueue(self,item):
        self.items.append(item)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

myq=Queue()
uq=Queue()
amyq=''
auq=''
score=0
inp=input("Enter Input : ").split(',')
i=inp[0]
amyq+=i[:3]
auq+=i[4:]
myq.enQueue(i[:3])
uq.enQueue(i[4:])

for i in range(1,len(inp)):
    amyq+=', '+inp[i][:3]
    auq+=', '+inp[i][4:]
    myq.enQueue(inp[i][:3])
    uq.enQueue(inp[i][4:])

print("My   Queue = "+amyq)
print("Your Queue = "+auq)
b=0
for a in myq.items:
    if a[0]==uq.items[b][0] and a[2]==uq.items[b][2]:
        score+=4
    elif a[2]==uq.items[b][2]:
        score+=2
    elif a[0]==uq.items[b][0]:
        score+=1
    else:
        score-=5
    b+=1


#set My Activity:Location ทั้งหมด
print("My   Activity:Location = ",end='')
x=myq.deQueue() #print My Activity:Location ตัวแรก
if x[0]=='0':
    print("Eat",end=':')
elif x[0]=='1':
    print("Game",end=':')
elif x[0]=='2':
    print("Learn",end=':')
elif x[0]=='3':
    print("Movie",end=':')

if x[2]=='0':
    print("Res.",end='')
elif x[2]=='1':
    print("ClassR.",end='')
elif x[2]=='2':
    print("SuperM.",end='')
elif x[2]=='3':
    print("Home",end='')

for j in range(1,len(inp)):
    y=myq.deQueue()
    if y[0]=='0':
        print(", Eat",end=':')
    elif y[0]=='1':
        print(", Game",end=':')
    elif y[0]=='2':
        print(", Learn",end=':')
    elif y[0]=='3':
        print(", Movie",end=':')

    if y[2]=='0':
        print("Res.",end='')
    elif y[2]=='1':
        print("ClassR.",end='')
    elif y[2]=='2':
        print("SuperM.",end='')
    elif y[2]=='3':
        print("Home",end='')
print()

print("Your Activity:Location = ",end='')
x=uq.deQueue() #print Your Activity:Location ตัวแรก
if x[0]=='0':
    print("Eat",end=':')
elif x[0]=='1':
    print("Game",end=':')
elif x[0]=='2':
    print("Learn",end=':')
elif x[0]=='3':
    print("Movie",end=':')

if x[2]=='0':
    print("Res.",end='')
elif x[2]=='1':
    print("ClassR.",end='')
elif x[2]=='2':
    print("SuperM.",end='')
elif x[2]=='3':
    print("Home",end='')

for j in range(1,len(inp)):
    y=uq.deQueue()
    if y[0]=='0':
        print(", Eat",end=':')
    elif y[0]=='1':
        print(", Game",end=':')
    elif y[0]=='2':
        print(", Learn",end=':')
    elif y[0]=='3':
        print(", Movie",end=':')

    if y[2]=='0':
        print("Res.",end='')
    elif y[2]=='1':
        print("ClassR.",end='')
    elif y[2]=='2':
        print("SuperM.",end='')
    elif y[2]=='3':
        print("Home",end='')
print()

if score>=7:
    print("Yes! You're my love! : Score is ",score,'.',sep='')
elif score>0 and score<7:
    print("Umm.. It's complicated relationship! : Score is ",score,'.',sep='')
else:
    print("No! We're just friends. : Score is ",score,'.',sep='')