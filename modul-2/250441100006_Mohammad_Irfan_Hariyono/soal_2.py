# beberapa harga dan diskon yang tercantum di dalam soal
tiket_normal = 50000
diskon_anak = 0.5
diskon_pelajar = 0.3
diskon_selasa = 0.2

# masukkan input pengguna
inp_usia = int(input("Masukkan usia mu : "))
status_pelajar = input("Apakah kamu pelajar SMA dengan kartu pelajar? (ya/tidak) : ").lower()
hari_beli = input("Masukkan hari : ").lower()

# menghitung diskon
diskon = 0.0

if inp_usia <= 12:
    diskon = diskon_anak
    print("Kamu mendapat diskon 50 %")
elif status_pelajar == "ya":
    diskon = diskon_pelajar
    print("Kamu mendapat diskon 30 %")
elif hari_beli == "selasa":
    diskon = diskon_selasa
    print("Kamu mendapat diskon 20 %")
else:
    print("Tidak ada diskon yang berlaku")
    
# operasi akhir
total_bayar = tiket_normal * (1 - diskon)

print("Jadi, Harga tiket yang harus dibayar: Rp", (int(total_bayar)))
