my_list = [1,2,3,4,5,6]
for i in my_list:

    print(i)

print(" Enumerate Demo below:\n ")

#Enumerate: Allows us to loop over something  and have an automatic counter. i is the automatic counter here.
# i - the automatic counter,starting with a value 0, by default. (Columnar/Vertical display of "i,element")
# element - the elements or values in my_list are printed out. (Columnar/Vertical display of "i, element")
for i, element in enumerate(my_list):
    print(i, element)
