def add(a,b):
    return a+b

a=int(input("enter n1:"))
b=int(input("enter n2:"))
res=add(a,b)
print(res)
#-------------------------------------------------------------------------------------------------------------------------------------

def area(b,h):
    return (1/2*b*h)
b=float(input("Enter base of triangle:"))
h=float(input("Enter height of triangle:"))
Area=area(b,h)
print("Area of triangle is:",Area)

#-------------------------------------------------------------------------------------------------------------------------------------

def si(p,r,t):
    return ((p*r*t)/100)
a=float(input("Enter the principal amount:"))
b=float(input("Enter the rate of intrest:"))
c=int(input("Enter the time period in years:"))
intrest=si(a,b,c)
print("The simple intrest is:",intrest)
#-------------------------------------------------------------------------------------------------------------------------------------


def bill(q,p):
    return q*p
q=int(input("Enter the quantity of items:"))
p=float(input("Enter the price per item:"))
Bill=bill(p,q)
print("Total bill amount is:",Bill)
#-------------------------------------------------------------------------------------------------------------------------------------


def fare(d,p):
    return d*p
d=float(input("Enter the distance in Km:"))
p=25
Fare=fare(d,p)
print("The fare of cab is:",Fare,"Rs.")
#-------------------------------------------------------------------------------------------------------------------------------------

def receipt():
    a=[]
    k=int(input("Enter the number of subjects:"))
    n=input("Enter your name:")
    r=input("registration no:")
    for i in range(k):
        s=input(f"Enter your subject name{i+1}:")
        a.append(s)
    print("Your exam details are:")    
    print("Name:",n)
    print("Registration no:",r)
    print("Subjects:",a)
        
receipt()
#-------------------------------------------------------------------------------------------------------------------------------------

def bill():
    a=input("Enter your bill amount:")
    b=float(a)
    t=(b-(0.1*b))
    print("Total bill amount is:",t)
bill()   
#-------------------------------------------------------------------------------------------------------------------------------------

def calories():
    c=float(input("Enter the carbs consumed in grams:"))
    f=float(input("Enter the fats cosumed in grams:"))
    p=float(input("Enter the proteins consumed in grams:"))

    calo=(c*4+f*9+4*p)
    print("Total amount of calories consumed is:",calo)

calories()

    









