while True:

    motor = input("Masukkan Jenis Motor (Matic/Trail/Sport): Motor ").lower()
    harga_motor = 0
    harga_diskon = 0
    diskon2 = 0
    asuransi = 15000
    hari = int(input("Masukkkan berapa hari penyewaan: "))
    matic = 50000
    trail = 100000
    total = 0
    sport = 150000
    
    if motor == "matic":
        print("Penyewaan Motor matic")
        harga_motor = matic * hari
        print(f"Harga Rental Motor Matic: {harga_motor}")
        
        if hari > 3:
            asuransi +=  asuransi
            print(f"Biaya asuransimu adalah: {asuransi}")
        else:
            print(f"Biaya asuransi : {asuransi} ")
        if harga_motor > 150000:
            diskon2 = harga_motor - (harga_motor * 0.1)
            diskon = input("Apakah kamu punya diskon? (ya/tidak): ")
        if diskon == "ya":
            diskon = input("Masukkan Kode diskon mu: ").lower()
            if diskon == "aconkgg":
                harga_diskon = harga_motor - (harga_motor * 0.05)
            else:
                print("Kode diskon salah!")
            
        total = diskon2 + harga_diskon        
        print(f"Total Harga adalah {total}")

    if motor == "trail":
        print("Penyewaan Motor Trail")
        harga_motor = trail * hari
        print(f"Harga Rental Motor Trail: {harga_motor}")
        
        if hari > 3:
            asuransi +=  asuransi
            print(f"Biaya asuransimu adalah: {asuransi}")
        else:
            print(f"Biaya asuransi : {asuransi} ")
        if harga_motor > 150000:
            diskon2 = harga_motor - (harga_motor * 0.1)
            diskon = input("Apakah kamu punya diskon? (ya/tidak): ")
        if diskon == "ya":
            diskon = input("Masukkan Kode diskon mu: ").lower()
            if diskon == "aconkgg":
                harga_diskon = harga_motor - (harga_motor * 0.05)
            else:
                print("Kode diskon salah!")
            
        total = diskon2 + harga_diskon        
        print(f"Total Harga adalah {total}")

    if motor == "sport":
        print("Penyewaan Motor Sport")
        harga_motor = sport * hari
        print(f"Harga Rental Motor Trail: {harga_motor}")
        
        if hari > 3:
            asuransi +=  asuransi
            print(f"Biaya asuransimu adalah: {asuransi}")
        else:
            print(f"Biaya asuransi : {asuransi} ")
        
        if harga_motor > 150000:
            diskon2 = harga_motor - (harga_motor * 0.1)
            diskon = input("Apakah kamu punya diskon? (ya/tidak): ")
        if diskon == "ya":
            diskon = input("Masukkan Kode diskon mu: ").lower()
            if diskon == "aconkgg":
                harga_diskon = harga_motor - (harga_motor * 0.05)
            else:
                print("Kode diskon salah!")
        print("="*40)
        total = diskon2 + harga_diskon        
        print(f"Total Harga adalah {total}")

    lagibang = input("Apakah ada penyewaan ulang? (ya/tidak): ")
    if lagibang != "ya":
        break

            

    
            
            



        
        
