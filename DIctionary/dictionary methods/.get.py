#used to avoid error line and continue to the next line .
#example

school = {
    "name" : "afrid",
    "subjects" : {
        "phy" : 90,
        "maths" : 77,
    },
    "rollno" : 24782
}
print(school["name2"]) #is we run this line now we get error because the keys is on existing in our keys
# this will stop the entire code to run like
#the code before print(school["name2"]) wil run and exicute but after print(school["name2"]) will not run because of the error  we got
#to avoid this we use .get()
print(school.get("name2")) #output : None
#if i print use .get() it will reuurn output as none and the other code the next line will run without any error
# that means the code the code will not stop if it gets error. If you use .get() function that could be implemented, even if the key is not present in the dictionary.