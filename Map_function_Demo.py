# map(): This function takes in a "function" and a "list" as parameters. The function(the first parameter in the map function) is applied to all the elements in the list and the result is returned in a new list.
#syntax: map(function, list)
#map(lambda function, list) is used along with a lambda function


my_list = [1,2,3,4]
squared_numbers=list(map(lambda x:x**2,my_list))
print(squared_numbers)


#Returning a cube of numbers
Cubed_Numbers=list(map(lambda y: y**3,my_list))
print(Cubed_Numbers)


#Output: 
[1, 4, 9, 16]
[1, 8, 27, 64]

Process finished with exit code 0
