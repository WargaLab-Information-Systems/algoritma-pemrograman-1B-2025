# input usia,status pelajar,hari
usia = int(input("masukkan usia : "))
status_pelajar = input("apakah anda pelajar SMA dengan kartu pelajar? (ya/tidak) : ")
hari = input("hari ini hari apa? : ")

# harga normal tiket
harga_normal_tiket = 50000

# diskon
diskon_anak_anak = 0.50 #50%
diskon_pelajar_SMA = 0.30 #30%
diskon_selasa = 0.20 #20%
diskon = 0

# kondisi diskon
# anak-anak < 12 tahun
if usia < 12:
    diskon = diskon_anak_anak
# pelajar SMA dengan kartu pelajar
if status_pelajar == "ya":
    diskon = diskon_pelajar_SMA
# penonton hari selasa (promo)
if hari == "selasa":
    diskon = diskon_selasa
# hitung harga akhir
harga_akhir = harga_normal_tiket * (1 - diskon)
# cetak harga tiket
print("harga tiket yang harus dibayar : Rp.",harga_akhir)
