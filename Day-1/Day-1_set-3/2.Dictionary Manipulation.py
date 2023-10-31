# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"











# Initialize an empty dictionary
ages = {}

# Function to add a new name-age pair
def add_name_age(name, age):
    ages[name] = age

# Function to update the age of a name
def update_age(name, new_age):
    if name in ages:
        ages[name] = new_age
    else:
        print(f"{name} does not exist in the dictionary.")

# Function to delete a name from the dictionary
def delete_name(name):
    if name in ages:
        del ages[name]
    else:
        print(f"{name} does not exist in the dictionary.")

# Example usage
add_name_age("John", 25)
print(ages)  # Output: {'John': 25}

update_age("John", 26)
print(ages)  # Output: {'John': 26}

delete_name("John")
print(ages)  # Output: {}
