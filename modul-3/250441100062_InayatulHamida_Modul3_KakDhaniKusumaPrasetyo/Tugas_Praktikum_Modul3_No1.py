n = int(input("Masukkan nilai n: "))

print(f"bilangan prima dari 1 sampai {n} adalah:")

for angka in range(2, n + 1):
    if angka == 2:
        print(angka)
    else:
        prima = True
        for i in range(2, angka):
            if angka % i == 0:
                prima = False
                break
        if prima:
            print(angka)
            