#2.Q find the greatest number among three numbers
# this way we can add 

num1,num2,num3 = int(input("enter the first number: ")), int(input("enter the second number: ")), int(input("enter the third number: "))
if num1 == num2 == num3:
    print("all numbers are equal")
elif num1>=num2 and num2>=num3:
    print("the first number is the greatest")
elif num3>=num3 :
    print("the second number is the greatest")
else:
    print("the third number is the greatest")# the output we get 