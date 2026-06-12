# Day 2 - Variables & Data Types

# Your personal info
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
is_student = True

# Do some math
age_in_10_years = age + 10
birth_year = 2026 - age

# Print everything out nicely
print("--- Your Profile ---")
print("Name: " + name)
print("City: " + city)
print("Age: " + str(age))
print("Are you a student?", is_student)
print("In 10 years you'll be:", age_in_10_years)
print("You were born in:", birth_year)