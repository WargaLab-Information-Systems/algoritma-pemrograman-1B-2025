print("masukkan jumlah nilai mahasiswa(0-100)")
nilai = int(input())
if nilai >= 0 and nilai <= 100:
    if nilai >= 85 and nilai <= 100:
        print("masukkan jumlah persen absensi")
        kehadiran = int(input())
        if kehadiran >= 90 and kehadiran <= 100:
            print("nilai A")
            print("Lulus dengan Pujian")
        else:
            print("nilai A")
    else:
        if nilai >= 70 and nilai <= 84:
            print("nilai B")
        else:
            if nilai >= 60 and nilai <= 69:
                print("nilai C")
            else:
                if nilai >= 50 and nilai <= 59:
                    print("nilai D")
                else:
                    if nilai < 50:
                        print("nilai E")
else:
    print("nilai tidak valid")
