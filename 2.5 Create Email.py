class CreateEmail():
    def __init__(self):
        self.firstname = None
        self.lastname = None

    def email(self):
        if self.firstname != None and self.lastname != None:
            return "'E' -> Email : " + self.firstname.lower() + '.' + self.lastname.lower() + "@kmitl.ac.th"
        elif self.firstname == None:
            return "'E' -> Email : Please Enter Your Firstname"
        elif self.lastname == None:
            return "'E' -> Email : Please Enter Your Lastname"
        else:
            return "'E' -> Fullname : Please Enter Your Firstname & Lastname"

    
    def add(self,f,l):
        self.firstname=f.lower()
        self.lastname=l.lower()
    
    def addfirstname(self,f):
        self.firstname=f.lower()

    def addlastname(self,l):
        self.lastname=l.lower()

    def showall(self):
        if self.firstname != None and self.lastname != None:
            fn=self.firstname[0].upper() + self.firstname[1:]
            ln=self.lastname[0].upper() + self.lastname[1:]
            return "'SA' -> Fullname : " + fn + ' ' + ln
        elif self.firstname == None and self.lastname == None:
            return "'SA' -> Fullname : Please Enter Your Firstname & Lastname"
        elif self.firstname == None:
            return "'SA' -> Fullname : Please Enter Your Firstname"
        elif self.lastname == None:
            return "'SA' -> Fullname : Please Enter Your Lastname"

    
    def showfirstname(self):
        if self.firstname != None:
            fn=self.firstname[0].upper() + self.firstname[1:]
            return "'SF' -> Firstname : " + fn
        else:
            return "'SF' -> Firstname : Please Enter Your Firstname"

    def showlastname(self):
        if self.lastname != None:
            ln=self.lastname[0].upper() + self.lastname[1:]
            return "'SL' -> Lastname : " + ln
        else:
            return "'SL' -> Lastname : Please Enter Your Lastname"




print("*** Create Email < BY KMITL > ***")
ce=CreateEmail()
inp = input("Enter Input : ").split(",")
for i in inp:
    if(i[0]=="E"):
        print(ce.email())
    elif(i[0]=="A"):
        x=i.split(" ")
        ce.add(x[1],x[2])
    elif(i[0]=="F"):
        x=i.split(" ")
        ce.addfirstname(x[1])
    elif(i[0]=="L"):
        x=i.split(" ")
        ce.addlastname(x[1])
    elif(i[:2]=="SA"):
        print(ce.showall())
    elif(i[:2]=="SF"):
        print(ce.showfirstname())
    elif(i[:2]=="SL"):
        print(ce.showlastname())
    elif(i[0]=="X"):
        break
    else:
        print("'" + i +"'" + ' is Invalid Input !!!')
        break
