harga_normal = 50000
diskon = 0
usia = int(input("Masukkan usia: "))
if usia <= 12 and usia >= 1 :
    print("anda seorang anak di bawah 12 tahun")
    diskon = 50
elif usia < 1 :
    print("umur anda tidak valid")
if usia >= 12 :
    status = input("Apakah anda seorang pelajar SMA dengan kartu pelajar? (ya/tidak): ")
    if status == "ya" :
        diskon = 30
hari = input("Masukkan hari: ")
if hari == "selasa":
        diskon = 20
harga_bayar = harga_normal - (harga_normal * diskon // 100)
print("harga yang harus anda bayar sebesar: ", harga_bayar)

