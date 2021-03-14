class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

print(" ***Decimal to Binary use Stack***")
s1= Stack()
ans=''
decNum= int(input("Enter decimal number : "))
while decNum!=0:
    newNum= decNum%2
    decNum = decNum//2
    s1.push(newNum)
while s1.size() != 0:
    ans+=str(s1.pop())
print("Binary number :",ans)