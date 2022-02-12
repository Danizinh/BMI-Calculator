print("******************************************************")
print("WELCOME TO BMI  CALCULATOR ")
print("******************************************************")
Peso = float(input("INFORME UM PESO:"))
Altura = float(input("INFORME UMA ALTURA"))
IMC = Peso / (Altura * Altura)
if (IMC < 18.5):
       print(f"{IMC:.5f} YOU ARE thin")
elif (IMC < 24.5):
        print(f"{IMC:.5f} YOU ARE normal")
elif (IMC < 29.9):
    print(f"{IMC:.5} YOU ARE overweight I")
elif (IMC < 34.9):
    print(f"{IMC:.5}YOU ARE obese I")
elif (IMC < 39.9):
    print(f"{IMC:.5}YOU ARE obese II")
elif(IMC > 40):
    print("YOU ARE morbidly obese III")

print("END TO CALCULATOR")