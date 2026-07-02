#list
marks = [45, 78, 98, 56, 89]
print(marks[1:4])#slicing
print(marks[2])
# we can change the string value here but not the integer value because string is immutable and integer is mutable
marks[2] = 100
print(list(marks)) #the output will be [45, 78, 100, 56, 89] because we changed the value of index 2 from 98 to 100
#but we cant change the value of string here


'''that means in stings we can change the value of string but not the individual character of string
because string is immutable and in list we can change the value of list and
also the individual element of list because list is mutable
'''

student = ["afrid", 20, "male"]
student[0] = "kumar"
print(list(student)) #output will[ 'kumar', 20, 'male']



