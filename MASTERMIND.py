# MASTER-MIND GAME---PROJECT 1
import sys


def digits1(n1, n2):
    l1=len(str(n1))
    l2=len(str(n2))
    a=list(str(n1))
    b=list(str(n2))
    z=0
    while (z!=(l2)):
        k=b[z]
        for i in range(l1):
            if (k==a[i]):
                print(k)
        z=z+1

def digits2(n1, n2):
    l1=len(str(n1))
    l2=len(str(n2))
    a=list(str(n1))
    b=list(str(n2))
    z=0
    while (z!=(l1)):
        k=a[z]
        for i in range(l2):
            if (k==b[i]):
                print(k)
        z=z+1

print("==========================================================================================================")
print("==================================== WELCOME TO THE MASTERMIND GAME ======================================")

print("PLAYER 1")
p1=int(input("ENTER A NUMBER:-"))
c1=0  # THE NUMBER OF TRIES FOR PLAYER 2 TO GUESS
c2=0 # THE NUMBER OF TRIES FOR PLAYER 1 TO GUESS
flag=0
flag1=0
x=0
y=0
print("PLAYER 2")
while (x==0):
    for i in range(c1+1):
        p2=int(input("GUESS THE NUMBER:-"))
        if (c1==0 and p1==p2):  # CONDITION WHERE PLAYER 2 GUESSES RIGHT AT FIRST TRY
            flag=1
            break
        elif (p1==p2):
            c1=c1+1
            x=2
            print("=====================================CONGRATULATIONS=========================================")
            print("                            *** THAT'S THE CORRECT NUMBER ***")
            print("=============================================================================================")
            print("THE NUMBER OF TRIES YOU TOOK:-", c1)
            break
        else:
            c1=c1+1
            print("THAT'S INCORRECT!!")
            print("*** HINTS ***")
            print("THE NUMBERS YOU GOT RIGHT ARE:-")
            digits1(p1, p2)
            print("TRY AGAIN")
            x=0
    if (flag == 1):
        break

if (flag==1):
    print("====================================================================================================")
    print("                                      !!!PLAYER 2 WINS!!!\n")
    print("                                   PLAYER 2 IS THE MASTERMIND")
    print("====================================================================================================")
    sys.exit()





print("========================================================================================================")
print("NOW PLAYER 2")
p3=int(input("ENTER A NUMBER:-"))

print("PLAYER 1")
while (y==0):
    for i in range(c2+1):
        p4=int(input("GUESS THE NUMBER:-"))
        if (c2==0 and p3==p4):  # CONDITION WHERE PLAYER 2 GUESSES RIGHT AT FIRST TRY
            flag1=1
            break
        elif (p3==p4):
            c2=c2+1
            y=2
            print("=====================================CONGRATULATIONS=========================================")
            print("                            *** THAT'S THE CORRECT NUMBER ***")
            print("=============================================================================================")
            print("THE NUMBER OF TRIES YOU TOOK:-", c2)
            break
        else:
            c2=c2+1
            print("THAT'S INCORRECT!!")
            print("*** HINTS ***")
            print("THE NUMBERS YOU GOT RIGHT ARE:-")
            digits2(p3, p4)
            print("TRY AGAIN")
            y=0
    if (flag1 == 1):
        break

if (flag1==1):
    print("====================================================================================================")
    print("                                      !!!PLAYER 1 WINS!!!\n")
    print("                                   PLAYER 1 IS THE MASTERMIND")
    print("====================================================================================================")
    sys.exit()


print("\n")
print("                                                 GAME OVER")
print("\n*******************************************************************************************************")
print("PLAYER 2 TOOK",c1,"TRIES TO GUESS THE NUMBER CORRECTLY")
print("PLAYER 1 TOOK",c2,"TRIES TO GUESS THE NUMBER CORRECTLY")
print("*********************************************************************************************************")

if (c1>c2):
    print("***********************************  PLAYER 1 IS MASTERMIND!!!  ************************************")
else:
    print("***********************************  PLAYER 2 IS MASTERMIND!!!  ************************************")