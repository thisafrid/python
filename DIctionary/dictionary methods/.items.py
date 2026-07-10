#used to get (keys,values) in pairs
#example

school = {
    "name" : "afrid",
    "subjects" : {
        "phy" : 90,
        "maths" : 77,
    },
    "rollno" : 24782
}
print(school.items()) #output : dict_items([('name', 'afrid'), ('subjects', {'phy': 90, 'maths': 77}), ('rollno', 24782)]) / in pairs
#also we can do this 
pair = list(school.items()) # we can create a new varaiable 
print(pair[0]) #and print any pair like pair[0]. output : ('name', 'afrid')