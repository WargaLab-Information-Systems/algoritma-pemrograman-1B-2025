1. # Harga per item
harga_buku_tulis = 5000
harga_pensil = 4500

# Jumlah item yang dibeli
jumlah_buku_tulis = 3
jumlah_pensil = 2

# Menghitung total harga sebelum pajak
total_harga_buku_tulis = harga_buku_tulis * jumlah_buku_tulis
total_harga_pensil = harga_pensil * jumlah_pensil
total_harga_sebelum_pajak = total_harga_buku_tulis + total_harga_pensil

# Menghitung pajak
pajak = 0.10 * total_harga_sebelum_pajak

# Menghitung total harga setelah pajak
total_harga_setelah_pajak = total_harga_sebelum_pajak + pajak

# Menampilkan hasil
print(f"Total belanja setelah pajak: Rp {total_harga_setelah_pajak:.2f}")