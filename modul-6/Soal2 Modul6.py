# Program penggabungan dua tuple tanpa duplikat

# Data awal
t1 = (3, 1, 4)
t2 = (1, 5, 9)

# --- Gabungkan kedua tuple ---
panjang_t1 = 0
for _ in t1:
    panjang_t1 += 1

panjang_t2 = 0
for _ in t2:
    panjang_t2 += 1

# Buat list baru hasil gabungan
gabung = [0] * (panjang_t1 + panjang_t2)
idx = 0

# Masukkan elemen t1
for i in range(panjang_t1):
    gabung[idx] = t1[i]
    idx += 1

# Masukkan elemen t2
for i in range(panjang_t2):
    gabung[idx] = t2[i]
    idx += 1

# --- Hapus duplikat ---
hasil_tanpa_duplikat = [0] * (panjang_t1 + panjang_t2)
panjang_hasil = 0

for i in range(idx):
    angka = gabung[i]
    sudah_ada = False
    for j in range(panjang_hasil):
        if hasil_tanpa_duplikat[j] == angka:
            sudah_ada = True
            break
    if not sudah_ada:
        hasil_tanpa_duplikat[panjang_hasil] = angka
        panjang_hasil += 1

# --- Urutkan descending ---
for i in range(panjang_hasil):
    for j in range(i + 1, panjang_hasil):
        if hasil_tanpa_duplikat[i] < hasil_tanpa_duplikat[j]:
            temp = hasil_tanpa_duplikat[i]
            hasil_tanpa_duplikat[i] = hasil_tanpa_duplikat[j]
            hasil_tanpa_duplikat[j] = temp

# --- Buat tuple hasil akhir ---
hasil_akhir = ()
for i in range(panjang_hasil):
    hasil_akhir = hasil_akhir + (hasil_tanpa_duplikat[i],)

# --- Tampilkan hasil ---
print("Tuple 1 :", t1)
print("Tuple 2 :", t2)
print("Hasil akhir setelah digabung, tanpa duplikat, dan diurutkan menurun:")
print(hasil_akhir)