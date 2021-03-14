class Stack():
    def __init__(self):
        self.l=[]

    def adder(self,value):
        self.l.append(value)
        return "Add = " + str(value) + " and Size = " + str(len(self.l))
    
    def pop(self):
        if self.l != []:
            x=self.l[-1]
            y=self.l.index(x)
            self.l.pop()
            return "Pop = " + str(x) + " and Index = " + str(y)
        else:
            return -1

stack=Stack()
inp=input("Enter Input : ").split(',')
for i in inp:
    if i[0]=='A':
        print(stack.adder(i[2:]))
    elif i[0]=='P':
        print(stack.pop())
if stack.l != []:
    a=' '
    for j in stack.l:
        a += str(j)+' '
    print("Value in Stack =" + a)
else:
    print("Value in Stack = Empty")