class Node:
  def __init__(self, item):
    self.item = item
    self.next = None
  def setNext(self, node):
    self.next = node
class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0 #ไม่มี
  def __str__(self):
    if self.size == 0:
      return 'Empty'
    else:
      s = ''
      cur = self.head
      for i in range(self.size - 1):
        s = s + str(cur.item) + ' '
        cur = cur.next
      s += str(self.indexOf(self.size - 1).item)
      return s
  #function -> remove
  def isEmpty(self):
    return self.size == 0
  def getSize(self):
    return self.size
  def indexOf(self, index):
    if index < self.size:
      cur = self.head
      for i in range(index):
        cur = cur.next
      return cur
    else:
      return 'Out of range'
  def addHead(self, newHead):#newHead = itemNode
    if self.isEmpty():
      self.head = Node(newHead)
    else:
      tmp = Node(newHead)
      tmp.setNext(self.head)
      self.head = tmp
    self.size += 1
  def append(self, newNode):
    if self.isEmpty():
      self.head = Node(newNode)
    else:
      cur = self.indexOf(self.size - 1)
      cur.setNext(Node(newNode))
    self.size += 1
  def insert(self, newNode, index):
    if index == self.size:
      self.append(newNode)
    elif index == 0:
      self.addHead(newNode)
    else:
      cur = self.indexOf(index - 1)
      tmp = cur.next
      cur.setNext(Node(newNode))
      cur.next.setNext(tmp)
      self.size += 1
  def index(self, itemCheck):
    cur = self.head
    count = 0
    while cur is not None:
      if cur.item == itemCheck:
        return count
      else:
        count += 1
        cur = cur.next
    return -1
  def search(self, item):
    index = self.index(item)
    if index == -1:
      return 'Not Found'
    else:
      return 'Found'
  def remove(self, index):
    if index < self.size and index > 0:
      cur = self.indexOf(index - 1)
      if cur.next.next is not None:
        cur.setNext(cur.next.next)
      else:
        cur.setNext(None)
      self.size -= 1
      return 'Success'
    elif index < self.size and index == 0:
      self.head = self.head.next
      self.size -= 1
      return 'Success'
    else:
      return 'Out of Range'
  def reverse(self):
    s = ''
    for i in range(self.size - 1,0,-1):
      s = s + str(self.indexOf(i).item) + ' '
    s += str(self.indexOf(0).item)
    return s

inpt=input('Enter Input (L1,L2) : ').split()
L1 = LinkedList()
L2 = LinkedList()
for i in inpt[0].split('->'):
    L1.append(i)
for i in inpt[1].split('->'):
    L2.addHead(i)
print('L1    : '+str(L1))
print('L2    : ',end='')
for i in inpt[1].split('->'):
    print(i+' ',end='')
print()
print('Merge : '+str(L1)+' '+str(L2))