# Harga tiket normal
harga_tiket = 50000
usia = int(input("Masukkan usia Anda: "))
if usia == -1:
  print("Usia tidak valid!!!")
else:
    diskon = 0 
    if usia < 12:
        hari = input("Masukkan hari: ")
        diskon = 50
        if hari == 'selasa':
            diskon = max(diskon, 50)
    else:
        pelajar = input("Apakah Anda pelajar SMA dengan kartu pelajar? (ya/tidak): ")
        hari = input("Masukkan hari: ")
        if pelajar == 'ya':
            diskon = max(diskon, 30)
        if hari == 'selasa':
            diskon = max(diskon, 20)

    harga_setelah_diskon = harga_tiket - (harga_tiket * diskon / 100)
    print(f"Harga tiket yang harus dibayar: Rp{int(harga_setelah_diskon):,}")
