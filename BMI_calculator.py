

Weight = int(input("Weight:"))
Height = int(input("Height :"))
BMI = (Weight *703)/(Height * Height)
print("Your BMI is " + str(BMI))
if BMI < 18.5:
        print("You are underweight and your Health risk is minimal")
elif 18.5 < BMI < 24.0 :
        print(" You are normal weight and your health risk is Minimal")
else:
    print("We will check you out")



