harga_buku = 5000
jumlah_buku = 3
harga_pensil = 4500
jumlah_pensil = 2

#Hitung total belanja sebelum pajak
total = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil) 
#Hitung pajak 10%
pajak = 0.10 * total

#Total bayar setelah pajak
total_bayar = total + pajak

print(f"Total belanja sebelum pajak: Rp{total}")
print(f"Pajak 10%: Rp{pajak}")
print(f"Total yang harus dibayar: Rp{total_bayar}")