peso = float(input("Qual é seu peso?(kg)"))
altura = float(input("Qual é sua altura(m)"))
IMC = peso / (altura * altura)
if (IMC < 18.5):
       print(f" PARABENS, você está ABAIXO do PESO NORMAL {IMC:.2f} ")
elif (IMC < 24.5):
        print(f"PARABENS,você está na Faixa de PESO normal {IMC:.2f}")
elif (IMC < 29.9):
    print(f" você está com  excesso de peso I {IMC:.2Ff}")
elif (IMC < 34.9):
    print(f" você está em OBESIDADE I {IMC:.2f}")
elif (IMC < 39.9):
    print(f" você está em OBESIDADE  II {IMC:.2f}")
elif(IMC > 40):
    print("você está em OBESIDADE MORBIDO  III")
