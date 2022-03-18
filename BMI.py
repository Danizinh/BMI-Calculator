print("******************************************************")
print("WELCOME TO BMI  CALCULATOR ")
print("******************************************************")
Weight = float(input("Enter your Weight:"))
Height = float(input("Enter your Height:"))
BMI = Weight / (Height * Height)
if (IMC < 18.5):
       print(f"{IMC:.5f} you are thin")
elif (IMC < 24.5):
        print(f"{IMC:.5f} you are normal")
elif (IMC < 29.9):
    print(f"{IMC:.5} you are overweight I")
elif (IMC < 34.9):
    print(f"{IMC:.5} you areobese I")
elif (IMC < 39.9):
    print(f"{IMC:.5} you areobese II")
elif(IMC > 40):
    print("YOU ARE morbidly obese III")

print("END TO CALCULATOR")