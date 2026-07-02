#1. tup.index()
#used to find the index of a specific element in the tuple
#2. tup.count()
#used to count the number of occurrences of a specific element in the tuple     

#example:
A = (1, 2, 3, 2, 5,6,3)
A.index(2)
A.index(3)
print(A.index(2)) #output will be 1 because the first occurrence of 2 is at index 1
print(A.index(3)) #output will be 2 because the first occurrence of 3 is at index 2
print(A.count(2)) #output will be 2 because 2 occurs 2 times in the tuple
