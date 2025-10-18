n = int(input("Masukkan nilai n: "))

print("Bilangan prima dari 1 sampai", n, "adalah:")

for angka in range(2, n + 1):
    prima = True
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break
    if prima:
        print(angka, " ")

        