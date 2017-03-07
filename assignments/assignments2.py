class AccountBalance():
    def processTransactions(self,startingBalance, transactions):
        a=0
        b=0
        for i in transactions:
            if('C' in i.split(" ")):
                a=a+int(i.split(" ")[1])
            else:
                b=b+int(i.split(" ")[1])
        return startingBalance+a-b
        
class AdditionGame(): 
    def getMaximumPoints(self,A, B, C, N):
        i=0
        FinalPoints=0
        while i<N:
            x=max(A,B,C)
            if(x>=1):
                x=max(A,B,C)
                FinalPoints=FinalPoints+x
                if(x==A):
                    A=A-1
                elif(x==B):
                    B=B-1
                else:
                    C=C-1
            else:
                FinalPoints=FinalPoints+x
            i=i+1
        return FinalPoints
class ATaleOfThreeCities():
    def connect(self, ax, ay, bx, by, cx, cy):
        import math
        n1=len(ax)
        n2=len(bx)
        n3=len(cx)
        temp1=math.sqrt((ax[0]-bx[0])**2+(ay[0]-by[0])**2)
        for i in range(0,n1):
            for j in range(0,n2):
                if(temp1>math.sqrt((ax[i]-bx[j])**2+(ay[i]-by[j])**2)):
                    temp1=math.sqrt((ax[i]-bx[j])**2+(ay[i]-by[j])**2)
        temp2=math.sqrt((ax[0]-cx[0])**2+(ay[0]-cy[0])**2)
        for i in range(0,n1):
            for j in range(0,n3):
                if(temp2>math.sqrt((ax[i]-cx[j])**2+(ay[i]-cy[j])**2)):
                    temp2=math.sqrt((ax[i]-cx[j])**2+(ay[i]-cy[j])**2)
        temp3=math.sqrt((cx[0]-bx[0])**2+(cy[0]-by[0])**2)
        for i in range(0,n3):
            for j in range(0,n2):
                if(temp3>math.sqrt((cx[i]-bx[j])**2+(cy[i]-by[j])**2)):
                    temp3=math.sqrt((cx[i]-bx[j])**2+(cy[i]-by[j])**2)
        return (temp1+temp2+temp3)-max(temp1,temp2,temp3)

class IntoTheMatrix():
    def takePills(self, turns, N):
        pass
