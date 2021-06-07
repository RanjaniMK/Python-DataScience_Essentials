tuple_1 =('MItch', 'Sandra', 'Luis', 1, 2, 3, 4)
#Tuple is immutable and the following assignment/alteration/change to the tuple is not allowed
tuple_1[1] = 'Lovely'

#Output: tuple_1[1] = 'Lovely'
#        TypeError: 'tuple' object does not support item assignment

#The following would throw up an error too.
     #tuple_1[4] = 10
     #print(tuple_1[4])
