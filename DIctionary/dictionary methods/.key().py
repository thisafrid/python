#Dictionary methods
#1. .key() - used to get all the keys in the dictionary (it only get keys of the main dictionary  not the nested dictionary)
#example

school = {
    "name" : "afrid",
    "subjects" : {
        "phy" : 90,
        "maths" : 77,
    },
    "rollno" : 24782
}

print(school.keys()) # got the keys and also we can 
print(list(school.keys())) #we can use list also
