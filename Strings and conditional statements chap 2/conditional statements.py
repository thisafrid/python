#if statement
age = int(input("Enter your age: "))
if age >= 18:
    Name = input("Enter your name: ")
    print("Hello " + Name)
    print("you can vote")
else:
    print("not eligible")


#else if statement
age = int(input("Enter your age: "))
if age >= 18:
    Name = input("Enter your name: ")
    print("Hello " + Name)
    print("you can drive")
elif age >= 16:
    print("you can drive cycle")  
else:
    print("not eligible")
