
while True:
    n1 = input("Masukkan jumlah elemen data pertama: ")
    if n1.isdigit():
        n1 = int(n1)
        break
    else:
        print("Input tidak valid. Silakan masukkan angka.")

data1 = []
for i in range(n1):
    while True:
        angka = input(f"Masukkan angka ke-{i+1} untuk data pertama: ")
        if angka.isdigit():
            data1.append(int(angka))
            break
        else:
            print("Input tidak valid. Silakan masukkan angka.")

while True:
    n2 = input("Masukkan jumlah elemen data kedua: ")
    if n2.isdigit():
        n2 = int(n2)
        break
    else:
        print("Input tidak valid. Silakan masukkan angka.")

data2 = []
for i in range(n2):
    while True:
        angka = input(f"Masukkan angka ke-{i+1} untuk data kedua: ")
        if angka.isdigit():
            data2.append(int(angka))
            break
        else:
            print("Input tidak valid. Silakan masukkan angka.")

gabungan = []
for x in data1:
    gabungan.append(x)
for x in data2:
    gabungan.append(x)

tanpa_duplikat = []
for angka in gabungan:
    if angka not in tanpa_duplikat:
        tanpa_duplikat.append(angka)

n = len(tanpa_duplikat)
for i in range(n):
    for j in range(0, n - i - 1):
        if tanpa_duplikat[j] < tanpa_duplikat[j + 1]:
            tanpa_duplikat[j], tanpa_duplikat[j + 1] = tanpa_duplikat[j + 1], tanpa_duplikat[j]

hasil_akhir = tuple(tanpa_duplikat)

print("\nHasil akhir:", hasil_akhir)

