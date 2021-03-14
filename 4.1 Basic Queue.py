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


q=Queue()
x=input('Enter Input : ').split(',')
for i in x:
    if i[0] == 'E':
        q.enQueue(i[2:])
        print("Add",i[2:],"index is",q.items.index(i[2:]))
    elif i[0] == 'D':
        if q.isEmpty():
            print(-1)
        else:
            print("Pop",q.deQueue(),"size in queue is",q.size())
if q.isEmpty():
    print("Empty")
else:
    print("Number in Queue is : ",q.items)
        

  