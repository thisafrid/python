'''Store following word meanings in a python dictionary :
table: "a piece of furniture", "list of facts & figures" 
cat: "a small animal" '''

dict = {
    "table" :{
        "table1" : "a piece of furniture",
        "table2" : "list of facts & figures",
    },
    "cat" : "a small animal",
}
print(dict["table"]) # output : {'table1': 'a piece of furniture', 'table2': 'list of facts & figures'}
print(dict["cat"]) #output : {'table1': a small animal