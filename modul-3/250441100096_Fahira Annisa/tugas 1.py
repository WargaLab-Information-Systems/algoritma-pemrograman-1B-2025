n = int(input("masukkan nilai bilangan prima: ")) 

print("bilangan prima dari 1 sampai n  adalah: ")
for angka in range(2, n +1):
    bilangan_prima = True
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            bilangan_prima = False
            break
    if  bilangan_prima:
            print(angka, " ")