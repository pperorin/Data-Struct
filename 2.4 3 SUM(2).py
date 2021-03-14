import itertools
strNumber = str(input('Enter Your List : ')).split(' ')
number,ans = [],[]
i = 0
for x in strNumber :
   number.append(int(x))
   i+=1
if i > 2 :
    for x in range(0,len(number)-2):
        for y in range(x+1,len(number)-1):      
            for z in range(y+1,len(number)):
                if(number[x] + number[y] + number[z]) == 5 and [number[x] , number[y] , number[z]] not in  ans :   
                    ans.append([number[x],number[y],number[z]])
    for j in ans:
        j.sort()
    ans = list(ans for ans,_ in itertools.groupby(ans))     
    print(ans)

else :
    print('Array Input Length Must More Than 2')