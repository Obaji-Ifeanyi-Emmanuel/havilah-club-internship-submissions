# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: your code here
name = "Obaji Ifeanyi Emmanuel"
age = 22
GPA = 3.5
is_student = True
print("Name", name)
print("Type of Name:", type(name))
print("Age:", age)
print("Type of Age:", type(age))
print("GPA:", GPA)
print("Type of GPA:", type(GPA))
print("Is Student:", is_student)
print("Type of Is_Student:", type(is_student))
# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: your code here
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}C is equal to {fahrenheit}F")

fahrenheit_input = float(input("Enter temperature in fahrenheit: "))
celsius_output = (fahrenheit_input - 32) * 5 / 9
print(f"{fahrenheit_input}F is equal to {celsius_output:.2f}C")

# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: your code here
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
year_turn_30 = birth_year + 30

print(f"Hello {name}!")
print(f"Your current age is {age} years.")
print(f"You will turn 30 in the year {year_turn_30}.")

# TODO: your code here for Robot censor monitor

robot_name = input("Enter Robot Name: ")
robot_id = input("Enter Robot ID: ")
sensor_name = input("Enter Sensor Name: ")
sensor_reading_str = input("Enter Sensor Reading: ")
operating_limit_str = input("Enter Operating Limit: ")

sensor_reading = float(sensor_reading_str)
operating_limit = float(operating_limit_str)

difference = operating_limit - sensor_reading

print("\n" + "=" * 30)
print("     ROBOT SENSOR REPORT     ")
print("=" * 30)
print(f"Robot Name     : {robot_name}")
print(f"Robot ID       : {robot_id}")
print(f"Sensor Name    : {sensor_name}")
print(f"Sensor Reading : {sensor_reading}")
print(f"Operating Limit: {operating_limit}")
print(f"Difference     : {difference}")
print("=" * 30)