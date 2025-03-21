t=0
s=0
class idd:
    def sanjaikumar(self,iid):
        self.iid=iid
yy=idd()     
class common:
        tflag=20
        pcount=0
        price=5000
        al=[]
        s=0
sanjai=common()
class Cashier:
    psng=1000
    psl=[]
    c=0
class Passen(common):
    def __init__(self,name,age,email,phone,gender,status):
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone
        self.gender=gender
        self.status="ticket is waiting"
    pas=False
def checkavailable():
    if(sanjai.pcount<sanjai.tflag):
        s=sanjai.tflag-sanjai.pcount
        print("\nTicket available is:",s)
    else:
        print("Ticket not available")
    print("Ticket price is : 5,000")
def amount():
    amt=0
    if(1<=sanjai.pcount):
        amt=sanjai.pcount*sanjai.price
        print("Total fare is:",amt)
        
def approve():
    if(sanjai.s==1):
        print("....Your Ticket Not yet Booked....")
    else:
        if(sanjai.pcount<sanjai.tflag):
            for i in range(len(sanjai.al)):
                sanjai.al[i].status="....Your Ticket is issued...."
            print("....Ticket is Approved....")
        else:
            print("....Your Ticket Not yet Booked....")
        
def cashlogin():
    while True:
        print("1.approve\n2.issue Ticket\n3.logout")
        n=int(input())
        s=0
        if(n==1):
            approve()
            sanjai.s+=1
            # sanjai.al.status=1
        elif(n==2):
            if(len(sanjai.al)==0):
                print("...............Ticket not yet booked..............")
            else:
                print('\n your id is:',yy.iid)
                for i in range(len(sanjai.al)):
                    print('your name is:',sanjai.al[i].name)
                    print('your age is:',sanjai.al[i].age)
                    print('your email is:',sanjai.al[i].email)
                    print('your phone is:',sanjai.al[i].phone)
                    print('your gender is:',sanjai.al[i].gender)
                    print('your status is:',sanjai.al[i].status)
                amount()
            print("...........Your Ticket is Issued............")
        else:
            break
def pasLogin():
    while True:
        print("1.check availability\n2.Book ticket\n3.fare\n4.passenger details\n5.cancel ticket\n6.sign out")
        n=int(input())
        if n==1:
            checkavailable()
        elif  n==2:
            print("How many tickets add :") 
            m=0
            m=int(input())
            for i in range(0,m):
                 n=input('your name is:\n')
                 nn=int(input('your age is:\n'))
                 nnn=input('your email is:\n')
                 nnnn=int(input('your phone is:\n'))
                 nnnnn=input('your gender is:\n')
                 status=0
                 suba=Passen(n,nn,nnn,nnnn,nnnnn,status)
                 sanjai.al.append(suba)
            sanjai.pcount+=m
            # print("ticket count is:",sanjai.pcount)
        elif n==3:
            print("ticket count is:",sanjai.pcount)
            print("your ticket amount is:", sanjai.pcount*sanjai.price)
        elif n==4:
            if(len(sanjai.al)==0):
                print("...............Ticket not yet booked..............")
            else:
                f=open("Passengerdetail.txt","w")
                print('\n your id is:',yy.iid)
                f.write(str(yy.iid)+"\n")
                for i in range(len(sanjai.al)):
                   print('your name is:',sanjai.al[i].name)
                   print('your age is:',sanjai.al[i].age)
                   print('your email is:',sanjai.al[i].email)
                   print('your phone is:',sanjai.al[i].phone)
                   print('your gender is:',sanjai.al[i].gender)
                   print('your status is:',sanjai.al[i].status)
                   f.write('your name is: '+sanjai.al[i].name+"\n"+'your age is:'+str(sanjai.al[i].age)+"\n"+'your email is:'+str(sanjai.al[i].email)+"\n"+'your phone is:'+str(sanjai.al[i].phone)+"\n"+'your gender is:'+str(sanjai.al[i].gender)+"\n"+'your status is:'+str(sanjai.al[i].status)+"\n")
                if(1<=sanjai.pcount):
                    amt=sanjai.pcount*sanjai.price
                    print("total fare is:",amt)
                f.write("total fare is:"+str(amt))
        elif n==5:
            print("do you want to cancel the ticket?")
            print("1.Yes\n2.No")
            m=int(input())
            if(m==1):
                sanjai.al=[]
                print("........your ticket has been cancelled.........")
            else:
                print(".........your ticket not yet cancelled.........")
        else:
            break
        
def __main__():
    print(" * * * WELCOME TO FLIGHT RESERVATION * * * ")
    while True:
        print("1.Login\n2.Exit")
        a=int(input())
        if a==1:
            while True:
                print("1.Passenger\n2.Cashier\n3.Back")
                b=int(input())
                if b==1:
                    while True:
                        print("1.Signup\n2.Signin\n3.Logout")
                        c=int(input())
                        if c==1:
                            print("Enter passenger Detail")
                            sl=[]
                            v=input("Enter Passenger Name: ")
                            sl.append(v)
                            yy.sanjaikumar(v)
                            sl.append(input("Create Password: "))
                            f=1
                            sl.append(Cashier.psng)
                            print("Your Registration number is:",Cashier.psng)
                            Cashier.psng+=1
                            sl.append(0)
                            sl.append("No Result")
                            Cashier.psl.append(sl)
                        elif c==2:
                            rg=int(input("Enter RegNo:\n"))
                            ps=input("Enter Password:\n")
                            if rg<1000 or Cashier.psng<=rg:
                                print("Passenger not found!")
                            else:
                                if Cashier.psl[rg-1000][1]==ps:
                                    pasLogin()
                                else:
                                    print("Password Mismatch")
                        else:
                           break
                elif b==2:
                        cashlogin()
                else:
                    break
        
        else:
            break 
__main__()
