#nesting - used to write if statement inside another if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("you can drive and vote")
    if age >= 59:
        print("you can  vote and drive")
    if age >= 60:
        print("you can  vote but not drive")
else:
    print("not eligible")
        