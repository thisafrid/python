#used to add elements
#we can add elements and delete elements in set .but we cant change the set 

#1. .add() - usd to add elements
#2. .remove() - to remove elements
#3. .clear() - to empyt the set
#4. .pop() = to remove random value
#5. .union() - use to combine two sets and create a new set .here it ignores duplicate values here.
#6. .intersection() - return the comman values from the two sets

numbers1 ={2,3,4,5,2,4,5,33,3,9}
numbers2 ={88,3,4,98,4,57,3,25,6}
names =set()

names.add("cricket")
names.add("rohith")
names.add(22)
names.remove(22)
names.pop()
print(names)
print(numbers1.union(numbers2)) #output : {33, 2, 3, 4, 5, 98, 6, 9, 88, 57, 25}
print(numbers1.intersection(numbers2)) #output : {3, 4}