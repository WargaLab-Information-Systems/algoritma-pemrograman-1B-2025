#tugas 1
pelanggan = input("Masukkan nama pelanggan: ")

# Barang pertama
jumlah_buku = 3
harga_buku = 5000
total_buku = jumlah_buku * harga_buku

# Barang kedua
jumlah_pensil = 2
harga_pensil = 4500
total_pensil = jumlah_pensil * harga_pensil

# Hitung total belanja
total_belanja = total_buku + total_pensil

# Tambahkan pajak 10%
pajak = total_belanja * 0.10
total_setelah_pajak = total_belanja + pajak

# Output
print(f"Total belanja {pelanggan} adalah Rp{total_belanja:,}")
print(f"Pajak (10%) adalah Rp{pajak:,.0f}")
print(f"Total yang harus dibayar adalah Rp{total_setelah_pajak:,.0f}")