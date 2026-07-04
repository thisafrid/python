#Problem Statement –
#Particulate matters are the biggest contributors to Delhi pollution. The main reason behind the
#increase in the concentration of PMs include vehicle emission by applying Odd Even concept for all
#types of vehicles. The vehicles with the odd last digit in the registration number will be allowed on
#roads on odd dates and those with even last digit will on even dates.
#Given an integer array a[], contains the last digit of the registration number of N vehicles traveling on
#date D(a positive integer). The task is to calculate the total fine collected by the traffic police
#department from the vehicles violating the rules.
#Note : For violating the rule, vehicles would be fined as X Rs....

A = []
Date = int(input("Enter the date:"))
Vdig1,Vdig2,Vdig3 =int(input("Enter the vechile number :")) ,int(input("Enter the vechile number:")) ,int(input("Enter the vechile number:"))
if Date%2 ==0 and Vdig%2 !=0:
    print("The vechicle is not allowed to drive")
elif Date%2 !=0 and Vdig%2 ==0:
    print("The vechicle is not allowed to drive")
else:
    print("The vechicle is allowed to drive")
print(A)