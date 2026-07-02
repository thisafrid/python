#to find whether the list is palindrome or not


list = [1,2,3,2,1]
list_copy = list.copy() #here we are making a copy of the list because if we reverse the original list then it will change the original list and we want to keep the original list as it is so we are making a copy of the list and then reversing the copy of the list
list_copy.reverse()
if list_copy == list:
    print("the list is palindrome")
else:
    print("the list is not palindrome") #output will be "the list is palindrome" because the list is same as its reverse