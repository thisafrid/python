#to find the number of students with a particular grade in a list of grades
#also to sort the list of grades in ascending order

grade = input("Enter the grade of the student: ")
Grades = ["c","d","a","a","b","b","a"]
Grades.sort() #for better representation of the grades in ascending order
print(Grades) #to print the list of grades in ascending order
print ("Number of students with grade", grade, ":", Grades.count(grade))
