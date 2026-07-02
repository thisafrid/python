#1 - list.append()
#used to add a new element at the end of the list
#2 - list.sort()
#used to sort the list in ascending order
#3 - list.sort(reverse = True)
#used to sort the list in descending order
#4 - list.reverse()
#used to reverse the list
#5 - list.insert()
#used to insert a new element at a specific index in the list
#list.Remove()
#used to remove a specific element from the list
#list.pop()
#used to remove the last element from the list


#example:
marks = [45, 78, 98, 56, 89]
names = ["afrid", "kumar", "rahul", "sachin"]
cars = ["bmw", "audi", "mercedes", "ferrari"] 
cars.reverse() #it will reverse the list

#we can also sort the list of strings in ascending and descending order
#it will sort by the first letter of each word .if the first letter in alphaetical order then it will sort by the second letter and so on
names.sort(reverse=True)
marks.append(100)
marks.sort() #for sorting the list in ascending order
marks.sort(reverse=True) #for sorting the list in descending order
cars.reverse() 
print(marks)
print(names)#output will be ['sachin', 'rahul', 'kumar', 'afrid'] because we sorted the list in descending order
print(cars) #output will be ['ferrari', 'mercedes', 'audi', 'bmw'] because we reversed the list

#insert() method is used to insert a new element at a specific index in the list
marks.insert(2, 22)
print(marks) #output will be [45, 78, 22, 98, 56, 89, 100] because we inserted the value 22 at index 2 in the list
