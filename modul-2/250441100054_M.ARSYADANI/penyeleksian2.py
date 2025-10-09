harga_normal = 50000

usia = int(input("Masukkan usia: "))
if usia <= 0 or usia >= 100:
    print("Usia tidak valid")
else:
    if usia < 15:
        status_pelajar = "tidak"
    else:
        status_pelajar = input("Apakah anda pelajar SMA dengan kartu pelajar? (ya/tidak): ")
    hari = input("Masukkan hari: ")
    diskon = 0

    if usia < 12:
        diskon = 50
    if status_pelajar == "ya":
        if 30 > diskon:
            diskon = 30
    if hari == "selasa":
         if 20 > diskon:
            diskon = 20

    bayar = harga_normal - (harga_normal * diskon // 100)

    print("Harga tiket yang harus dibayar: Rp", bayar)
