#str.endswith()
#return true if the string ends with the word mentioned in the function.
#example

str = "iam going to watch salman khan movie"
print(str.endswith("vie")) #output True 
print(str.endswith("ing")) #output False


#str.capitalize()
#used to capitilize the first letter in a string
str = "iam going to watch salman khan movie"
str = str.capitalize() #to make the first letter capital every time i print we can use this
print(str.capitalize())
 # it gives output as "Iam going to watch salman khan movie"
#if i print normal str now 
print(str) # i get "iam going to watch salman khan movie"

str = str.capitalize() #to make the first letter capital every time i print we can use this




#str.replace(old,new)
#used to replace the word or a letter 
str = "iam going to watch salman khan movie"
str = str.replace("salman","sohail")
print(str) #we get "iam going to watch sohail khan movie" 



#str.find(word)
#used to find the word or letter , it returns the first index of the first occurrer
str = "iam going to watch salman khan movie"
print(str.find("movie")) #output "31"

#str.count()
#findes the number of times the word has occured 
str = "iam going to watch salman khan movie"
print(str.count("watch")) #return 1 time
print(str.count("a")) #5