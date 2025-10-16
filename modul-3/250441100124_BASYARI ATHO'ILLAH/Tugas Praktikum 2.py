pin = input("Buat Pin ATM mu (XXYYY): ")

if not pin.isdigit() or len(pin) != 5: 
    print("PIN harus berupa angka dan 5 digit")
    
else:
    coba = input("Apakah sudah ingat pin mu? (ya/tidak): ").lower()
    percobaan = 0
    max_coba = 3
    if coba == "ya":
        while percobaan < max_coba:
            pin2 = input("Masukkan PIN: ")
            percobaan += 1
            
            if pin2 == pin:
                print("PIN ANDA BENAR!!")
                break
            else:
                if percobaan < max_coba:
                    print(f"PIN salah, Kesempatan tinggal {max_coba - percobaan}")
                else:
                    print("ATM ANDA TERBLOKIR")
    else:  
        print("Gitu doang lupa")


