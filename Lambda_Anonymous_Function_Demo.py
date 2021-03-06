#A typical function with a name can be written as below:
#def squared(x):
#    return x**2

#FUNCTION CALL:

#print(squared(2))
#print(squared(4))

# Executing the above same function alternatively using an anonymous function called lambda
# lambda function is generally used with filter() and map() functions.
# SYNTAX: map( lambda function, list)
# SYNTAX: filter(lambda function, list)

y= lambda x:x**2

#Calling the function
y(4)
print(y(4))
print(y(10))


#Output: 16    100 (Columnar Display)
