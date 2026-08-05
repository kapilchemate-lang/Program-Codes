print("Program to display the average marks and grade of students")

N=int(input("Enter the number of students in class:"))  #Taking the input for number of students in class

totalmarks=0
Avg=0
ovag=0

                                                               #Looping for number of students and calculating their average marks and grade
for j in range (1,(N+1)):    
    for i in range(1,6):
         marks=int(input(f"Enter the marks in subject{i} :"))      
         totalmarks=totalmarks+marks                           #Calculating totalmarks of a student 
    print("Total marks scored are:",totalmarks)
    
    Avg=totalmarks/5                                           #Calculating the  average marks of a student
    print("Average marks scored are:",Avg)
   
    percentage=(totalmarks/250)*100                            #Calculating the  percentage of a student  
    print(f"Percentage of student{j} is:",percentage)

                                                               #Displaying the grade of a student    
    if(60<=percentage<70):
         print("You scored 'C' grade")
    elif(70<=percentage<80):
         print("You scored 'B' grade")
    elif(80<=percentage<90):
         print("You scored 'A' grade")
    elif(percentage>=90): 
         print("You scored 'O' grade")
    else:              
         print("You scored 'E' grade")   
    totalmarks=0;       
    ovag=ovag+Avg  
    overallaverage=ovag/N  
print("Overall average marks of class is:",overallaverage)     #Displaying the Average marks of the class