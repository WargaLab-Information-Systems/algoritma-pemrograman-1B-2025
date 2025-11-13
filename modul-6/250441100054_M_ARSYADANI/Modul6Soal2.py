tuple_pertama = (3, 1, 4)
tuple_kedua = (1, 5, 9)

gabungan = tuple_pertama + tuple_kedua

daftar_unik = []
for angka in gabungan:
    if angka not in daftar_unik:
        daftar_unik.append(angka)

n = len(daftar_unik)
for i in range(n):
    for j in range(0, n - i - 1):
        if daftar_unik[j] < daftar_unik[j + 1]:
            # Tukar posisi
            daftar_unik[j], daftar_unik[j + 1] = daftar_unik[j + 1], daftar_unik[j]

hasil_akhir = tuple(daftar_unik)
print("Hasil akhir:", hasil_akhir)