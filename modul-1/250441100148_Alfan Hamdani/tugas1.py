# Menghitung total belanja ATK (Alat Tulis Kantor)
harga_buku = 5000 #harga satuan
jumlah_buku = 3

harga_pensil = 4500 #harga satuan
jumlah_pensil = 2

pajak_persen = 10 #persen

total_buku = harga_buku * jumlah_buku
total_pensil = harga_pensil * jumlah_pensil

total_pajak = (total_buku + total_pensil) // pajak_persen

total_bayar = (total_buku + total_pensil) + total_pajak

print("Harga 3 Buku : Rp.",total_buku)
print("Harga 2 Pensil : Rp.",total_pensil)
print("Pajak : Rp.",total_pajak)
print("Harga Setelah Pajak : Rp.",total_bayar)