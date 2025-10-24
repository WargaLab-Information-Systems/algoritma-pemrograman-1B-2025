durasi_parkir = int(input("Mau berapa jam kamu ingin memarkir kendaraan = "))
vip = input("Apakah kamu member vip? (ya/tidak) : ").lower()
#code lower() disini saya pakai untuk mengubah semua char dalam string jadi huruf kecil
#jika saya tidak memakai lower() string bersifat case-sensitive

biaya_2_jam = 5000
biaya_per_jam = 3000
biaya_per_hari = 20000

if vip == "ya":
    total_biaya = 0
    print("Karena kamu pengguna vip, Maka ")
else:
    if durasi_parkir <=2:
        total_biaya = biaya_2_jam
    else:
        total_biaya = biaya_2_jam + (durasi_parkir - 2) * biaya_per_jam
        if total_biaya > biaya_per_hari:
            total_biaya = biaya_per_hari
print("Total pembayaran parkir: Rp", total_biaya)