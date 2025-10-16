pin = int(input("Masukkan PIN :"))

for i in range(3):

    pin_input = input("Masukkan PIN anda :")
    if pin_input == pin:
        print("PIN yang anda masukkan benar , akses diterima")
        break
    else :
        if i < 2 :
            print("PIN yang anda masukkan salah ,coba lagi ")
        else:
            print("Akses ditolak,kartu anda diblokir hahaha")

    
