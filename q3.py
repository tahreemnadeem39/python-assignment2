#Q3-Fahrenheit to Celsius

# Prompt the user for a temperature in Fahrenheit
degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert the temperature to Celsius using the formula
degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# Output the temperature in the desired format
print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

