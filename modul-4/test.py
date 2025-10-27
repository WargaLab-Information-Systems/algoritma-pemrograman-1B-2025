# buat seleksi kondisi jika nilai a = 80 - 90, b = 70 - 80, c = 60 - 70, d = 50 - 60, sisanya e
# input ga boleh lebih dari 100
 
nilai = int(input("Masukan Nilai : ")) 
if nilai > 90:
    print("Nilai Tidak Valid")

elif nilai <= 90 and nilai >= 80 :
    print("Nilai A")

elif nilai <= 79 and nilai >= 70 :
        print("Nilai B")

elif nilai <= 69 and nilai >= 60 :
        print("Nilai C")

elif nilai <= 59 and nilai >= 50 :
        print("Nilai D")
else :
    if nilai < 50 :
        print("Nilai E")