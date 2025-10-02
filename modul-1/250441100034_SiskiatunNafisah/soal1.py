print("MENGHITUNG TOTAL BELANJA HALLIM ")

jumlah_buku = 3
harga_buku = 5000
jumlah_pensil = 2
harga_pensil = 4500
pajak_persen = 10
total_buku = jumlah_buku * harga_buku
total_pensil = jumlah_pensil * harga_pensil
total_sebelum_pajak = total_buku + total_pensil
pajak = total_sebelum_pajak * (pajak_persen / 100)
total_bayar = total_sebelum_pajak + pajak

print("Total harga buku:", total_buku)
print("Total harga pensil:", total_pensil)
print("Total belanja hallim sebelum pajak:", total_sebelum_pajak)
print("Pajak (10%):", pajak)
print("Total yang harus dibayar hallim:", total_bayar)