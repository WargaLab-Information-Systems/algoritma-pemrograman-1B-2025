# variabel nya
buku_tulis = 5000
jumlah_buku = 3
pensil = 4500
jumlah_pensil = 2
pajak_tiap_barang = 0.10

#operator aritmatika
harga_buku_tulis = buku_tulis * jumlah_buku
harga_pensil = pensil * jumlah_pensil
total_harga_semua = harga_buku_tulis + harga_pensil
pajak = total_harga_semua * pajak_tiap_barang
total_ditambah_pajak = total_harga_semua + pajak

#menampilkan hasil nya
print("Total harga sebelum ditambah pajak adalah Rp", total_harga_semua)
print("Pajak dari total harga barang sebesar Rp", pajak)
print("Total harga setelah ditambah pajak adalah Rp", total_ditambah_pajak)