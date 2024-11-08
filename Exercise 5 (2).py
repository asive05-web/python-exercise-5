# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits

fruits = ["apple", "banana", "cherry"]
# TODO: Add a fruit to the end of the list
fruits.append("orange")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, "kiwi")
# TODO: Remove a fruit from the list
fruits.remove("banana")
# TODO: Print the modified list

print(fruits)
#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]
# TODO: Create a new list with each number squared
squared_numbers = [num ** 2 for num in numbers]
# TODO: Find the sum and average of the original numbers
total_sum = sum(numbers)
average = total_sum / len(numbers)
# TODO: Print the results
print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)
print("Sum:", total_sum)
print("Average:", average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitalss

african_countries_capitals = {
    "Nigeria": "Abuja",
    "Egypt": "Cairo",
    "South Africa": "Pretoria",
    "Kenya": "Nairobi"
}

# TODO: Add a new country-capital pair

african_countries_capitals["Ghana"] = "Accra"

# TODO: Update the capital of an existing country

african_countries_capitals["South Africa"] = "Cape Town"

# TODO: Remove a country-capital pair

del african_countries_capitals["Egypt"]

# TODO: Print the modified dictionary

print(african_countries_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
# Create a dictionary of fruit colors
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange",
    "kiwi": "brown"
}

# TODO: Print all the fruits (keys)
# Print all the fruits (keys)
print("Fruits:", list(fruit_colors.keys()))

# TODO: Print all the colors (values)
# Print all the colors (values)
print("Colors:", list(fruit_colors.values()))

# TODO: Print each fruit and its color
# Print each fruit and its color
for fruit, color in fruit_colors.items():
    print(f"{fruit}: {color}")

# TODO: Check if a fruit is in the dictionary and print its color
# Check if a fruit is in the dictionary and print its color
fruit_to_check = "banana"
if fruit_to_check in fruit_colors:
    print(f"The color of {fruit_to_check} is {fruit_colors[fruit_to_check]}.")
else:
    print(f"{fruit_to_check} is not in the dictionary.")
