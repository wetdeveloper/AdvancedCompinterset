

def compound_interest(P, R, T):
    Amount = P * (pow((1 + R / 100), T))  
    CI=Amount-P
    # Printing & Returning The Simple Interest	
   # print('The Compound Interest Is', CI,'Currencies')
    return CI
# Recieving The Data From The User
P=float(input("Enter The Principle : "))
duration=int(input("how many days?"))
interest=float(input("what interest?"))
#T=float(input("Enter The Rate Of Interest : "))
#R=float(input("Enter The Time Duration : "))
positionVolume=float(input("how much $ per position")) #maximum opend position size is 100$ for example
if P>positionVolume:
    mop=float(P/positionVolume)#maximum openable position number
    daycounter=1
    while(daycounter!=duration):
       P+=compound_interest(positionVolume,1,interest)*mop #R=1 because we trade each position one time per day
       if int(P/positionVolume)>int(mop):#to pervent to have like mop=20.63
            mop=float(P/positionVolume)
       interestsMade=compound_interest(positionVolume,1,interest)
       print(f"Ballance:{P} ------PositionVolume:{positionVolume}---Positions:{mop}---Intersets Made:{interestsMade} per position ---totall interests made:{interestsMade*mop}")
       daycounter+=1
else:
    print("Try again")
    exit
 

# Finding Out The Simpl Interest
#compound_interest(P,R,T)
