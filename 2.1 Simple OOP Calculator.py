def findMinimum(l):
    if len(l) == 1:
       return l[0]
    else:
       return min(l[0], findMinimum(l[1:]))

x=list(map(int,input('Enter Input : ').split()))
print('Min :',findMinimum(x))