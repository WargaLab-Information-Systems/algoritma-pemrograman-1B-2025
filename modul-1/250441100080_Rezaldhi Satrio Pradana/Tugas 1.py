harga_buku_tulis = int(5000) 
jumlah_buku_tulis = int(3)
print("total harga buku tulis =", (harga_buku_tulis) *
(jumlah_buku_tulis))
#TOTAL HARGA PENSIL
harga_pensil = int(4500)
jumlah_pensil = int(2)
print("total harga pensil =", (harga_pensil) * (jumlah_pensil))
#TOTAL SEBELUM PAJAK
total_harga_bukudanpensil = (harga_buku_tulis) * (jumlah_buku_tulis) + (harga_pensil) * (jumlah_pensil)
print("harga sebelum pajak =", (harga_buku_tulis) *
(jumlah_buku_tulis) + (harga_pensil) * (jumlah_pensil))
#TOTAL SETELAH PAJAK
pajak = float(0.10)
print(total_harga_bukudanpensil * pajak)
#TOTAL BIAYA YANG HARUS DI BAYAR KE KASIR
total_setelah_pajak = float(26400.0)
print(total_setelah_pajak)