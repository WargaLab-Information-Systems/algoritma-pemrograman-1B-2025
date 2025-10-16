Pin = "25018"
k = 0  

while k < 5:
    pin = input("masukkan PIN anda: ")  
    
    banyak = 0
    for panjang in pin:
        banyak += 1
    
    if banyak != 5:
        print("PIN harus 5 digit! ulangi lagi.")
    
    acc = True
    for percobaan in pin:
        if percobaan <'0' or percobaan >= '9':
            acc = False
    
    if not acc:
        print("PIN harus angka, tidak boleh huruf atau simbol.")
        break

    elif pin == Pin:
        print("PIN benar, akses diterima")
        akses_diterima = True  
        break

    else:
        k += 1
        K = 5 - k
        if K > 0:
            print(f"PIN salah, coba lagi kesempatan anda masih {K} ")
        
else:
    print("Akses ditolak, kartu diblokir")
