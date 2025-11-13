pin_awal = input("Buat pin ATM anda (XXYYY): ")
kesempatan = 3 

if not pin_awal.isdigit() or len(pin_awal) != 5:
    print("Pin harus berupa angka dan terdiri dari 5 digit.")

else:
    yakin = input("Apakah anda yakin dengan pin anda? (ya/tidak): ").lower()
    if yakin == "ya":
        while kesempatan > 0:
            pin_input = input("Masukkan pin ATM anda: ")
            if pin_input == pin_awal:
                print("Pin benar. Akses diterima.")
                break
            else:
                kesempatan -= 1
                if kesempatan > 0:
                    print(f"Pin salah. Anda memiliki {kesempatan} kesempatan lagi.")
                else:
                    print("Pin salah. Akun diblokir.")        