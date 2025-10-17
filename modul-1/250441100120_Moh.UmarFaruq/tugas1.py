# Soal 1
# Harga satuan buku dan pensil
harga_buku = 5000
harga_pensil = 4500

# jumlah buku dan pensil yang dibeli
jumlah_buku = 3
jumlah_pensil = 2

# menghitung total harga buku dan pensil
total_harga_buku = harga_buku * jumlah_buku
total_harga_pensil = harga_pensil * jumlah_pensil

# menghitung total harga sebelum pajak
total_harga_sebelum_pajak = total_harga_buku + total_harga_pensil

# menghitung pajak 10%
pajak = total_harga_sebelum_pajak * 0.10

# Menghitung total harga setelah pajak
total_harga_setelah_pajak = total_harga_sebelum_pajak + pajak

a = ("jadi, Hallim harus membayar Rp. 26.400 ke kasir setelah ditambahkan pajak.")

# menampilkan hasil
print("Total harga buku : Rp.", total_harga_buku)
print("Total harga pensil : Rp.", total_harga_pensil)
print("Total harga sebelum pajak : Rp.", total_harga_sebelum_pajak)
print("Pajak 10% : Rp.",pajak)
print("Total harga setelah pajak : Rp.", total_harga_setelah_pajak)
print(a)


