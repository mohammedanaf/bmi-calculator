# Greet user with a welcome message
print("Welcome to BMI(Body Mass Index) Calculator\n")

# Ask user for their weight and height. Also; store it inside suitable variables.
weight = float(input("What is your weight? (in kilograms)\n"))
height = float(input("What is your height? (in meters)\n"))

# Calculate the bmi score by applying necessary logic. Hint: weight divided by height squared.
bmi = (weight / height ** 2)

# Round the bmi score to not more than two decimal places
bmi = round(bmi, 2)

# Display the output on the screen
print(bmi)
