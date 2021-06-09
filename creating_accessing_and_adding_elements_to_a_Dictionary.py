#In Dictionary: Elements are stored in a key-value pair format.

#Dictionary elements are accessed via keys like how List elements are accessed by their respective index.


# Defining a dictionary:

ranj_dict = {"Name" : "Ranjani",
             "Sex": "Female",
             "Sexual Orientation": "Straight",
             "Occupation": "Engineer",
            "Current_Year": 2021}


#Accessing a dictionary element by using it's key and printing out the same later:
ranj_dict["Name"]


print(ranj_dict["Name"])
#Ouput: Ranjani

#Adding a key-value pair:
ranj_dict["University"]="TU Darmstadt"

#Printing out the dictionary key-value pairs to check if the newest k,v pair -> University: TU Darmstadt is added.
print(ranj_dict)

#Output: {'Name': 'Ranjani', 'Sex': 'Female', 'Sexual Orientation': 'Straight', 'Occupation': 'Engineer', 'Current_Year': 2021, 'University': 'TU Darmstadt'}
