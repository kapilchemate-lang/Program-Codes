print("USE OF INBUILT FUNCTIONS MIN(),MAX(),POW(),LEN(),UPPER(),LOWER()")

#Entering a string
a="Good Morning"

#Entering the numbers as input
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

#calculating the max number
c=max(n1,n2)

#calculating the min number
d=min(n1,n2)

#calculating the exponent
e=pow(n1,n2)

#calculating the length of string
f=len(a)


#Displaying the results of above functions
print(f"The maximum among {n1} and {n2} is:",c)
print(f"The minimum among {n1} and {n2} is:",d)
print(f"The exponent of {n1} to {n2} is:",e)
print(f"The length of string {a} is:",f)
print(f"The lower case of string {a} will be:",a.upper())
print(f"The upper case of string {a} will be:",a.lower())

