t1 = (3, 1, 4, 11)
t2 = (1, 5, 9, 12)

# 1. Gabungkan kedua tuple
gabungan = t1 + t2

# 2. Hapus duplikat tetapi tetap mempertahankan urutan awal
hasil_tanpa_duplikat = []
for angka in gabungan:
    if angka not in hasil_tanpa_duplikat:
        hasil_tanpa_duplikat.append(angka)

# 3. Urutkan secara menurun (descending) tanpa sorted
for i in range(len(hasil_tanpa_duplikat)):
    for j in range(i + 1, len(hasil_tanpa_duplikat)):
        if hasil_tanpa_duplikat[i] < hasil_tanpa_duplikat[j]:
            # Tukar posisi
            hasil_tanpa_duplikat[i], hasil_tanpa_duplikat[j] = hasil_tanpa_duplikat[j], hasil_tanpa_duplikat[i]

# 4. Ubah kembali ke bentuk tuple
hasil_akhir = tuple(hasil_tanpa_duplikat)

print("Hasil akhir:", hasil_akhir)
