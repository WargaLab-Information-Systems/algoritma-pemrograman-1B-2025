n = int(input("Cari bilangan prima sampai: "))

print(f"Bilangan prima 1 sampai {n} adalah:")

for angka in range(2, n + 1):

    is_prima = True

    for pembagi in range(2, angka):

        if angka % pembagi == 0:
            
            is_prima = False
            break

    if is_prima:
        print(angka)