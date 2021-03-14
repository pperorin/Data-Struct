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

    def checkDuplicate(self):
        checklist = list(dict.fromkeys(self.items))
        for k in checklist:
            if self.items.count(k) > 1:
                return "Duplicate"
        return "NO Duplicate"

inp = input("Enter Input : ").split("/")
a=list(inp[0].split(" "))
b=list(inp[1].split(","))
q=Queue()
for i in a:
    q.enQueue(i)
for j in b:
    if j[0] == 'E':
        q.enQueue(j[2:])
    elif j[0]== 'D':
        q.deQueue()
print(q.checkDuplicate())