print("******************************************************")
print("WELCOME TO BMI  CALCULATOR ")
print("******************************************************")
Weight = float(input("Enter your Weight:"))
Height = float(input("Enter your Height:"))
BMI = Weight / (Height * Height)
if (BMI < 18.5):
       print(f"{IMC:.5f} you are thin")
elif (BMI < 24.5):
        print(f"{IMC:.5f} you are normal")
elif (BMI < 29.9):
    print(f"{IMC:.5} you are overweight I")
elif (BMI < 34.9):
    print(f"{IMC:.5} you areobese I")
elif (BMI < 39.9):
    print(f"{IMC:.5} you areobese II")
elif(BMI > 40):
    print("YOU ARE morbidly obese III")

print("END TO CALCULATOR")