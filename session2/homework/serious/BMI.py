print("this is the program that calculate your BMI")
m = float(input("enter your weight in kg:"))
height = float(input("enter your height in cm "))
h = height/100
BMI = m/(h*h)
print(BMI)
if BMI < 16:
    print("you are severely underweight")
elif 16 < BMI < 18.5:
    print("you are underweight")
elif 18.5 < BMI < 25:
    print("you are normal")
elif 25 < BMI < 30:
    print("you are overweight")
else:
    print("you are obese")