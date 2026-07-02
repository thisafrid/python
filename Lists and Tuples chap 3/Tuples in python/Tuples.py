#Tuple - an ordered, immutable collection of elements in Python .that means we can not change the value of tuple once it is created
#tuple is defined by using () round brackets
#tuple is used to store multiple items in a single variable

#example:
Marks = (45, 78, 98, 56, 89) #here after adding a number in list we need to put , 
#because if we dont put , then it will consider the number as integer and not as tuple
print(Marks)


#if here we dont put , then it will consider the number as integer and not as tuple
#example:
Name =("afrid")
print(Name)
print(type(Name)) #output will be <class 'str'> because we didnt put , after the string so it will consider the string as string and not as tuple
car =("bmw",) #here we put , after the string so it will consider the string as tuple and not as string
print(car)
print(type(car)) #output will be <class 'tuple'> because we put , after the string so it will consider the string as tuple and not as string


#here the tuple is immutable that means we can not change the value of tuple once it is created
#example
A = (1, 2, 3, 4, 5)
print(A[2:4])
A[2] =10 #output will be TypeError: 'tuple' object does not support item assignment because we can not change the value of tuple once it is created
