class TorKham:
    def __init__(self):
        self.words=[]

    def restart(self):
        self.words=[]
        return "game restarted"

    def play(self, word):
        if self.words == []:
            self.words.append(word)
            return self.words
        else:
            if self.words[-1][-2:].lower() == word[:2].lower():
                self.words.append(word)
                return self.words
            else:
                return "game over"
    
    

torkham = TorKham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
for i in S:
    if i[0]=="P":
        print('\'',i[2:],'\'',' -> ',torkham.play(i[2:]),sep='')
    elif i[0]=="R":
        print(torkham.restart())
    elif i[0]=="X":
        break
    else:
        print('\'',i,'\''," is Invalid Input !!!",sep='')
        break
