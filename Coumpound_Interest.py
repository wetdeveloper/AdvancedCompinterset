

def compound_interest(P, R, T):
    Amount = P * (pow((1 + R / 100), T))  
    CI=Amount-P
 
    return CI

P=float(input("Enter The Principle : "))
duration=int(input("how many days?"))
interest=float(input("what interest?"))

positionVolume=float(input("how much $ per position")) #maximum opend position size is 100$ for example
positionsperday=2
automaticposinc=False #Automatic increase of the positions number
if P>positionVolume:
    daycounter=1
    while(daycounter!=duration):
       if automaticposinc:
            mop=int(P/positionVolume)#maximum openable position number
            P+=compound_interest(positionVolume,1,interest)*mop #R=1 because we trade each position one time per day
       else:
            P+=compound_interest(positionVolume,1,interest)*positionsperday #R=1 because we trade each position one time per day
            mop=positionsperday
       interestsMade=compound_interest(positionVolume,1,interest)
       print(f"Ballance:{P} ------PositionVolume:{positionVolume}---Positions:{mop}---Intersets Made:{interestsMade} per position ---totall interests made:{interestsMade*mop}")
       daycounter+=1
else:
    print("Try again")
    exit
 

# Finding Out The Simpl Interest
#compound_interest(P,R,T)
