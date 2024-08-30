aves = ["Loro gris", "Paloma de diamante", "Coctel"]

VAI = ["Mayna", "Periquitos", "Cacatua"] #Valores A Ingresar

print("Los valores de la lista antes de insertar:")

for i in aves:
    print(i, end = " ")

print("\n")

for i in VAI:
    aves.append(i)
    
print("""
Los valores de la lista despues de insertar:""")

for j in aves:
    print(j, end = " ")
    
print("\n")