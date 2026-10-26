import Fundamentos

print("Programa que te demuestra si tu peso es correcto o es malo")

peso = float(input("Introduce tu peso: "))

if(peso <= 50):
    print("Su peso es normal y no tiene sobrepeso")
elif(peso >= 51):
    Fundamentos.PesoTest()