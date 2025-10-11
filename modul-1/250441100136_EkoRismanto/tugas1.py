# Belanja ke Toko ATK

buku = 5000
pensil = 4500
pajak = 10 #persen

bayar_buku = 5000 * 3
bayar_pensil = 4500 * 2
bayar_pajak = (bayar_buku + bayar_pensil) // 10
total_bayar = (bayar_buku + bayar_pensil) + bayar_pajak
print("Harga 3 Buku : Rp", bayar_buku, "Rupiah")
print("Harga 2 Pensil : Rp", bayar_pensil, "Rupiah")
print("Harga Pajak : Rp", bayar_pajak, "Rupiah")
print("Harga Setelah Pajak : Rp", total_bayar, "Rupiah")