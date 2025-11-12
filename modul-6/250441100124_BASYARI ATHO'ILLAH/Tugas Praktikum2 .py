tuple1 = (1,2,3,6,7,4)
tuple2 = (input("angka"))
print(f"Deret Pertama: {tuple1}")
print(f"Deret Kedua: {tuple2}")

gabungan = tuple1 + tuple2
print("Gabungan tanpa duplikat:", gabungan)

tanpa_duplikat = []
for angka in gabungan:
    if angka not in tanpa_duplikat:
        tanpa_duplikat.append(angka)
print("Tanpa duplikat:", tanpa_duplikat)

for i in range(len(tanpa_duplikat)):
    angka_terbesar = i
    for j in range(i + 1, len(tanpa_duplikat)):
        if tanpa_duplikat[j] > tanpa_duplikat[angka_terbesar]:
            angka_terbesar = j
    tanpa_duplikat[i], tanpa_duplikat[angka_terbesar] = tanpa_duplikat[angka_terbesar], tanpa_duplikat[i]

hasil_akhir = tuple(tanpa_duplikat)
print("Hasil akhir (urut menurun):", hasil_akhir)
