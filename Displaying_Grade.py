print("Program to calculate the percentage and display the grade")

print("Enter the marks score in following subject")

a1=int(input("Enter the marks scored in SF "))
a2=int(input("Enter the marks scored in PAI "))
a3=int(input("Enter the marks scored in DBMS "))
a4=int(input("Enter the marks scored in DSA "))
a5=int(input("Enter the marks scored in ECONOMICS "))

#Calculatin total marks
total=a1+a2+a3+a4+a5
print("Total marks scored out of 250 are:",total)

#Calculating percentage
percent=(total/250)*100
print("Percentage scored is:",percent)

#Displaying the grade according to the percentage
if(60<=percent<70):
	print("You scored 'C' grade")
elif(70<=percent<80):
	print("You scored 'B' grade")
elif(80<=percent<90):
	print("You scored 'A' grade")
elif(90<=percent):
	print("You scored 'A+' grade")
else:
	print("'D' Grade")	
