# 1. # Harga per item
# harga_buku_tulis = 5000
# harga_pensil = 4500

# # Jumlah item yang dibeli
# jumlah_buku_tulis = 3
# jumlah_pensil = 2

# # Menghitung total harga sebelum pajak
# total_harga_buku_tulis = harga_buku_tulis * jumlah_buku_tulis
# total_harga_pensil = harga_pensil * jumlah_pensil
# total_harga_sebelum_pajak = total_harga_buku_tulis + total_harga_pensil

# # Menghitung pajak
# pajak = 0.10 * total_harga_sebelum_pajak

# # Menghitung total harga setelah pajak
# total_harga_setelah_pajak = total_harga_sebelum_pajak + pajak

# # Menampilkan hasil
# print(f"Total belanja setelah pajak: Rp {total_harga_setelah_pajak:.2f}")

# 2. # Ukuran balok
# panjang_balok = 10  # cm
# lebar_balok = 6     # cm
# tinggi_balok = 4    # cm

# panjang = int(input("masukkan panjang balok(cm): "))
# lebar = int(input("masukkan lebar balok(cm): "))
# tinggi = int(input("masukkan tinggi balok(cm): "))

# # Menghitung volume
# volume = panjang_balok * lebar_balok * tinggi_balok

# # Menghitung luas permukaan
# luas_permukaan = 2 * (panjang_balok * lebar_balok + panjang_balok * tinggi_balok + panjang_balok * tinggi_balok)

# # Menampilkan hasil
# print(f"Volume balok: {volume} cm³")
# print(f"Luas permukaan balok: {luas_permukaan} cm²")

3. # Total bola
bola_merah = 8
bola_biru = 6
total_bola = 14

# jumlah bola yang diambil
r = 3

# hitungan permutasi (urutan hitung)
permutasi = total_bola * (total_bola - 1) * (total_bola - 2)

# hitung susun 3 bola
susun = r*(r-1)*1

# hasil
kombinasi = permutasi//susun

print("jumlah_bola_yang_diambil",r,"bola =", kombinasi)
