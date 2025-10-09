jam_parkir = int(input("Masukkan lama parkir (jam): "))
#tambahin seleksian jam
if jam_parkir == 0:
    print("Tidak memarkirkan mobil")
else:
    status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

    if status_vip == "ya":
        biaya = 0
    else:
        if jam_parkir <= 2:
            biaya = 5000
        elif jam_parkir <= 24:
            biaya = 5000 + (jam_parkir - 2) * 3000
            if biaya > 20000:
                biaya = 20000
    
        else:
            hari_penuh = jam_parkir // 24
            sisa_jam = jam_parkir % 24
            biaya = hari_penuh * 20000
            if sisa_jam > 0:
                if sisa_jam <= 2:
                    biaya += 5000
                else:
                    biaya += 5000 + (sisa_jam - 2) * 3000
                    if biaya > (hari_penuh + 1) * 20000:
                        biaya = (hari_penuh + 1) * 20000
    print("Total biaya parkir: Rp", biaya)
