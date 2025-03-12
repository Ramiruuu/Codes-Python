# 1. Creating tuples with different data types
my_tuple = (10, "hello", 3.14, True)
print("Tuple with different data types:", my_tuple)

# 2. Nested Tuple
nested_tuple = (1, (2, 3), (4, (5, 6)))
print("Nested tuple:", nested_tuple)
print("Accessing nested value:", nested_tuple[2][1][1])  # Output: 6

# 3. Tuple unpacking
person = ("John", 25, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# 4. Looping through a tuple
colors = ("red", "green", "blue")
print("Colors in the tuple:")
for color in colors:
    print(color)

# 5. Creating a single-element tuple
single_tuple = ("hello",)  # Needs a comma
print("Single-element tuple:", single_tuple)

# 6. Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Concatenated tuple:", merged_tuple)

# 7. Repeating tuples
repeated_tuple = tuple1 * 2
print("Repeated tuple:", repeated_tuple)

# 8. Checking if an element exists in a tuple
numbers = (10, 20, 30, 40)
print("Is 20 in numbers?", 20 in numbers)  # Output: True
print("Is 50 in numbers?", 50 in numbers)  # Output: False