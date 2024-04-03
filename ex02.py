#Calcular delta e avaliar raizes
a = float(input("Informe a: "))
b = float(input("Informe b: "))
c = float(input("Informe c: "))

#Cálulo do delta
delta = b**2 - (4*a*c)
#Avaliar as raízes
if delta > 0:
    print(f"Como delta é: {delta}, as raízes são reais e distintas ")
elif delta == 0:
    print(f"Como delta é: {delta}, as raízes são reais e iguais ")
elif delta < 0:
    print(f"Como delta é: {delta}, as raízes são imaginárias conjugadas ")

aaaa