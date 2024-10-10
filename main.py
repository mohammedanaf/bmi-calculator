# Greet user with a welcome message
print("Welcome to BMI(Body Mass Index) Calculator\n")

# Ask user for their weight and height. Also; store it inside suitable variables.
weight = float(input("What is your weight? (in kilograms)\n"))
height = float(input("What is your height? (in meters)\n"))

# Calculate the bmi score by applying necessary logic. Hint: weight divided by height squared.
bmi = (weight / height ** 2)

# Round the bmi score to not more than two decimal places
bmi = round(bmi, 2)

# Use conditional statements and display BMI score with its interpretation
if bmi < 18.5: # Less than 18.5
    print(f"Your BMI score is {bmi} and you are Underweight.")
elif bmi < 25: # Ranging between 18.5 and 25(not included)
    print(f"Your BMI score is {bmi} and you have Healthy Weight.")
elif bmi < 30: # Ranging between 25 and 30(not included)
    print(f"Your BMI score is {bmi} and you are Overweight.")
else:
    if bmi < 35: # Ranging between 30 and 35(not included)
        print(f"Your BMI score is {bmi} and you are Obese Class-1.")
    elif bmi < 40: # Ranging between 35 and 40(not included)
        print(f"Your BMI score is {bmi} and you are Obese Class-2.")
    else: # More than 40(included)
        print(f"Your BMI score is {bmi} and you are Obese Class-3.")
