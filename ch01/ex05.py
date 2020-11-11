'''Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.'''

# How to convert Celsius to Fahrenheit
# The temperature T in degrees Fahrenheit (°F) is equal to the temperature T in degrees Celsius (°C) times 9/5 plus 32:
# T(°F) = T(°C) × 9/5 + 32
# or
# T(°F) = T(°C) × 1.8 + 32

cels=float(input('enter you  Celsius temperature: '))
fahrenheit=cels*9/5+32 
print("fahrenheit: ",fahrenheit)