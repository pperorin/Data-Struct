class Queue():
    def __init__(self,lst = None):
        self.lst = lst if lst is not None else []
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return len(self.lst) == 0
    def top(self):
        return self.lst[0]
    def enQ(self,obj):
        self.lst.append(obj)
    def deQ(self):
        return self.lst.pop(0)
    def show(self):
        return self.lst
    def shownum(self,num):
        return self.lst[int(num)]

inp=input('Enter people and time : ').split()
Q = Queue()
Q1,Q2 = Queue(),Queue()
num1,num2=0,0
for i in inp[0]:
    Q.enQ(i)
for i in range(1,int(inp[1])+1):
    if num1 == 3:
        Q1.deQ()
        num1=0
    if num2 == 2:
        Q2.deQ()
        num2=0
    if Q1.size() < 5:
        if Q.isEmpty() == False:
            Q1.enQ(Q.deQ()) 
    else:
        if Q.isEmpty() == False:
            Q2.enQ(Q.deQ())
    if Q1.isEmpty() == False:
        num1+=1
    if Q2.isEmpty() == False:
        num2+=1
    print(str(i) + ' ',end='')
    print(Q.show(),end='')
    print(' ',end='')
    print(Q1.show(),end='')
    print(' ',end='')
    print(Q2.show())