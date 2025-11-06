#  Buat function dengan 3 parameter

def dana(iuran, darurat, pribadi):
    dana_keseluruhan = iuran + darurat + pribadi
    return dana_keseluruhan

iuran = int(input("Masukan Dana Iuran : "))
darurat = int(input("Masukan Dana Darurat : "))
pribadi = int(input("Masukan Dana Pribadi : "))

dana_keseluruhan = dana(iuran, darurat, pribadi)
print("Jadi total dana keseluruhan adalah : ", dana_keseluruhan)