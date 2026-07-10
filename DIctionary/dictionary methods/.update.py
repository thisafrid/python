#used to insert new value in a key and also to add new key to the dictonary
#example
from types import new_class


school = {
    "name" : "afrid",
    "subjects" : {
        "phy" : 90,
        "maths" : 77,
    },
    "rollno" : 24782
}
school.update({"name" : "kumar"})
school.update({"mobile" : 1234567890})
print(school["name"])#we can update the values in te existing key
print(school["mobile"])#we can also add new keys and assign values to it
print(school) #final output : {'name': 'kumar', 'subjects': {'phy': 90, 'maths': 77}, 'rollno': 24782, 'mobile': 1234567890}
#and also we can do like this
games = {"cricket" : "rohith"} #we can add new keys like this also. and add multiple keys with , 
print(school.update(games))
print(school) #output : {'name': 'kumar', 'subjects': {'phy': 90, 'maths': 77}, 'rollno': 24782, 'mobile': 1234567890, 'cricket': 'rohith'}
