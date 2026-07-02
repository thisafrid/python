#WAP to ask the user to enter names of their 3 favorite movies & store them in a list and then sort the list in ascending order and print the sorted list

MOVIE1 = input("Enter the movie 1 name :" )
MOVIE2 = input("Enter the movie 2 name :" )
MOVIE3 = input("Enter the movie 3 name :" )
list = [MOVIE1, MOVIE2, MOVIE3]
list.sort()
print("movies in ascending order:" ,list)

