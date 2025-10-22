# input maksimal angka yang akan dipakai
angka_maksimal = int(input("masukkan angka maksimal: "))

print("bilangan prima dari 1 sampai", angka_maksimal, "adalah: ")
# proses menentukan bilangan prima
for angka in range(2, angka_maksimal + 1):
    apakah_bil_prima = True
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            apakah_bil_prima = False
            break
    if apakah_bil_prima:
        print(angka, " ")