class Stack:
    def __init__(self,lst = None):
        self.lst = lst if lst is not None else []
    def push(self,item):
        self.lst.append(item)
    def pop(self):
        self.lst.pop()
    def peek(self):
        return self.lst[-1]
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return len(self.lst) == 0
    def remove(self,item):
        self.lst.remove(item)
    def lststack(self):
        return self.lst

inpt = input('Enter expresion : ')
op = ['{','[','(']
cl = ['}',']',')']
st=Stack()
st1=Stack()
for i in inpt:
    if i in op:
       st.push(i)   
    elif i in cl:
        if i == '}':
            if '{' in st.lststack():
                st.remove('{')
            else:
                st1.push(i)
        elif i == ']':
            if '[' in st.lststack():
                st.remove('[')
            else:
                st1.push(i)
        else:
            if '(' in st.lststack():
                st.remove('(')
            else:
                st1.push(i)
if st.isEmpty() and st1.isEmpty():
    for f in inpt:
        print(f,end='')
    print(' MATCH')
elif st.isEmpty():
    for a in inpt:
        print(a,end='')
    print(' close paren excess')
elif st1.isEmpty():
    for b in inpt:
        print(b,end='')
    print(' open paren excess   '+str(st.size())+' : ',end='')
    for c in st.lststack():
        print(c,end='')
else:
    for d in st.lststack():
        print(d,end='')
    for e in st1.lststack():
        print(e,end='')
    print(' Unmatch open-close')