#3.Q find the greatest number among four numbers


num1,num2,num3,num4 = int(input("enter the first number: ")), int(input("enter the second number: ")), int(input("enter the third number: ")), int(input("enter the fourth number: "))
if num1==num2==num3==num4:
    print("all numbers are equal")
elif num1>=num2 and num2>=3 and num3>=num4:
    print("the first number is the greatest")
elif num2>=num3 and num3>=num4:
    print("the second number is the greatest") 
elif num3>=num4:
    print("the third number is the greatest")

else:
    print("the fourth number is the greatest")