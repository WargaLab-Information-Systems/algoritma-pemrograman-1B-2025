while True:
    print("=== RENTAL MOTOR ACONK ===")
    print("1. Motor Matic  = Rp 50.000")
    print("2. Motor Trail  = Rp 100.000")
    print("3. Motor Sport  = Rp 75.000")

    pilihan = input("Pilih jenis motor (1/2/3): ")
    if pilihan == "1":
        jenis = "Matic"
        harga = 50000
    elif pilihan == "2":
        jenis = "Trail"
        harga = 100000
    elif pilihan == "3":
        jenis = "Sport"
        harga = 75000
    else:
        print("Pilihan tidak valid!")
        continue

    hari = int(input("Masukkan lama sewa (hari): "))

    subtotal = harga * hari

    if hari > 3:
        asuransi = (hari // 3) * 15000
    else:
        asuransi = 0

    total = subtotal + asuransi

    if subtotal > 150000:
        diskon1 = total * 0.10
    else:
        diskon1 = 0

    total -= diskon1

    kupon = input("Masukkan kupon (jika ada): ")
    if kupon == "AconkGG":
        diskon2 = total * 0.05
    else:
        diskon2 = 0

    total -= diskon2

    print("=== STRUK RENTAL MOTOR ACONK ===")
    print("Jenis Motor     :", jenis)
    print("Lama Sewa       :", hari, "hari")
    print("Subtotal        : Rp", subtotal)
    print("Asuransi        : Rp", asuransi)
    print("Diskon 10%      : Rp", int(diskon1))
    print("Diskon Kupon 5% : Rp", int(diskon2))
    print("-------------------------------")
    print("Total Bayar     : Rp", int(total))
    print("===============================")

    ulang = input("Apakah ingin menyewa lagi? (y/n): ")
    if ulang == "n":
        print("Terima kasih telah menggunakan Rental Motor Aconk!")
        break