'''WAP to enter marks of 3 subjects from the user and store them in a 
dictionary. Start with an empty dictionary & add one by one. 
Use subject name as key & marks as value.'''

Marks = {}
a = int(input("enter marks of phy:"))
Marks.update({"phy" : a})
b = int(input("enter marks of math:"))
Marks.update({"math" : b})
c = int(input("enter marks of bio:"))
Marks.update({"bio" : c})
print(Marks)

'''output :enter marks of phy:45
           enter marks of math:55
           enter marks of bio:67
            {'phy': 45, 'math': 55, 'bio': 67}'''