lanjut = "y"

while lanjut == "y":
    while True:
        lanjut = input("apakah anda ingin sewa motor (y/n)?")
        if lanjut == "n":
            break
        
        penyewaan = input("masukkan motor yang ingin di sewa:")
        if penyewaan == "motor matic":
            harga = 50000
        elif penyewaan == "motor trail":
            harga = 100000
        else:
            harga = 75000

        sewa = int(input("ingin disewa berapa hari:"))
        if sewa == 3:
            asuransi = 15000
            print("asuransi yang anda bayar :", asuransi)
        elif sewa > 3:
            A = 15000 * sewa
            print("asuransi yang anda bayar :", A)

        kupon = input("masukkan kupon yang anda miliki?")

        total = harga * sewa 
        print("harga sebelum diskon di masukkan :", total)

        if total >= 150000:
            diskon = 0.1
            d = total * diskon
            ts = total + d
            print("total harga diskon jika total semua lebih dari 150000 :", ts)
            if kupon == "AconkGG":
                diskon = 0.05
                d = ts * diskon
                ts = ts + d
                print("total harga diskon jika anda memiliki kupon + lebih dari 150000 :", ts)
            else:
                continue

