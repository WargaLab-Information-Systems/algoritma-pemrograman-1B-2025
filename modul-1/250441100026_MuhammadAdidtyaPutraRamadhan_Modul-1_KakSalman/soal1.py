buku_tulis = 3
harga_buku_tulis = 5000
pensil = 2
harga_pensil = 4500
pajak = 10

total_harga = (buku_tulis * harga_buku_tulis) + (pensil * harga_pensil)
total_pajak = total_harga * pajak
total_bayar = total_harga + total_pajak

print("Total harga sebelum pajak Rp:", total_harga)
print("Pajak (10%) Rp:", total_pajak)
print("Total harga yang dibayar Rp:", total_bayar)