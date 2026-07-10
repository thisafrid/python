'''Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)'''

#methd 1
set ={9,"9.0"}
print(set)


#method2
set ={
    "int":9,
    "float":9.0,
    }
print(set)