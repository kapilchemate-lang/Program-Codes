print("Program for list of assignments")

#Printing the list of subjects of current assignments
ass=['DSA','PAI','DBMS','Software Engineering']
print("The list of subjects of whose assignment is to be performed:-",ass)

#Printing the status of assignment that is/are completed
print("Assignment that is completed is/are 'PAI'")

#Removing the assignment that is completed
ass.remove('PAI')
print("Assignments that are left are:-",ass)

#Adding new assignment to list
ass.append('Economics')
print("New assignment added is 'Economics'")

#Printing the status of list of assignments that are remained
print("Assignment which are to be performed",ass)

#Clearing the list after completing the list of assignments
ass.clear()
print("Well done,you have completed all assignments",ass)