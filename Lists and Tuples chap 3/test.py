#with this is is 
list =[]
num = [1,2,3]
num1 =[3,2,1]
list.append(num+num1)
copy_num1 =num1.copy()
copy_num1.reverse()
#this is for 
if num == copy_num1:
    print("its a palindrom ",num+num1)
else:
    print("not palindrom ",list) #this
