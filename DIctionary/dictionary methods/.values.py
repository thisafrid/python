#used to get values of the keys in the dic
#example
school = {
    "name" : "afrid",
    "subjects" : {
        "phy" : 90,
        "maths" : 77,
    },
    "rollno" : 24782
}
print(school.values()) #we get output : dict_values(['afrid', {'phy': 90, 'maths': 77}, 24782])
print(list(school.values())) #output : ['afrid', {'phy': 90, 'maths': 77}, 24782] 
#here we get values of the nested keys also.