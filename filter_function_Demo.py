# filter() performs an operation on a list based on a specific condition.
# SYNTAX : filter( lambda function with a condition, list)

age_list =[20, 50, 22, 18, 7, 10]
# People only equal to or above the age of 21 can drink.

can_drink=list(filter(lambda x: x>=21, age_list))
print(can_drink)


#Ouput:

[50, 22]

Process finished with exit code 0

