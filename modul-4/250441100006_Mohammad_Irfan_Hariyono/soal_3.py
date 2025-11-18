print(" Program Piramida  Cermin pas Bjirka gabut ")

while True:
    n_string = input("Masukkan nilai n (misal : 5): ")

    inputan_adalah_angka_valid = True

    if n_string == "":
        inputan_adalah_angka_valid = False
    else:
        for karakter in n_string:
            if karakter not in "0123456789":
                inputan_adalah_angka_valid = False
                break
    if inputan_adalah_angka_valid:
        n = int(n_string)

        if n > 0:
            break
        else:
            print("Hemmm error guys Nilai n mu harus lebih besar dari 0. try on bruh ")
    else:
        print("Hemmm error lah input mu itu loh harus angka bulat positif (1, 2, 3...)")

print("=" * 30)

for i in range (n, 0, -1):

    for j in range (1, i + 1):
        if j < 10:
            print(j, end="  ")
        else:
            print(j, end=" ")


    jumlah_spasi_ditengah = 6 * (n - i)

    for k in range(jumlah_spasi_ditengah):
        print(" ", end="")

    for l in range (i, 0, -1):
        if l < 10:
            print(l, end="  ")
        else:
            print(l, end=" ")

    print()

print("=" * 30)
print("Pola mu selesai bjirka, semoga kamu tenang yaa😊")