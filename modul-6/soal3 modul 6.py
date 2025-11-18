def tampilkan_menu():
    print("\n=== PROGRAM SZOBOSZLAI ===")
    print("1. Tambah Angka (Create)")
    print("2. Tampilkan List (Read)")
    print("3. Ubah Angka (Update)")
    print("4. Hapus Angka (Delete)")
    print("5. Cek Apakah Bisa Dibagi Sama")
    print("6. Keluar")

def tambah_angka(daftar_angka):
    try:
        angka = int(input("\nMasukkan angka yang ingin ditambahkan: "))
        daftar_angka.append(angka)
        print(f"Angka {angka} berhasil ditambahkan!")
    except ValueError:
        print("Input tidak valid! Masukkan angka.")

def tampilkan_list(daftar_angka):
    if not daftar_angka:
        print("\nList masih kosong.")
    else:
        print(f"\nDaftar angka: {daftar_angka}")
        print(f"Total elemen: {len(daftar_angka)}")

def ubah_angka(daftar_angka):
    if not daftar_angka:
        print("\nList masih kosong.")
        return
    
    tampilkan_list(daftar_angka)
    try:
        indeks = int(input("\nMasukkan indeks yang ingin diubah (0-{}): ".format(len(daftar_angka)-1)))
        
        if 0 <= indeks < len(daftar_angka):
            angka_baru = int(input("Masukkan angka baru: "))
            angka_lama = daftar_angka[indeks]
            daftar_angka[indeks] = angka_baru
            print(f"Angka pada indeks {indeks} berhasil diubah dari {angka_lama} menjadi {angka_baru}!")
        else:
            print("Indeks tidak valid!")
    except ValueError:
        print("Input tidak valid!")

def hapus_angka(daftar_angka):
    if not daftar_angka:
        print("\nList masih kosong.")
        return
    
    tampilkan_list(daftar_angka)
    try:
        indeks = int(input("\nMasukkan indeks yang ingin dihapus (0-{}): ".format(len(daftar_angka)-1)))
        
        if 0 <= indeks < len(daftar_angka):
            angka_hapus = daftar_angka.pop(indeks)
            print(f"Angka {angka_hapus} pada indeks {indeks} berhasil dihapus!")
        else:
            print("Indeks tidak valid!")
    except ValueError:
        print("Input tidak valid!")

def cek_pembagian_sama(daftar_angka):

    if not daftar_angka:
        print("\nList masih kosong.")
        return
    
    print(f"\nDaftar angka: {daftar_angka}")
    
    total = 0
    for angka in daftar_angka:
        total += angka
    
    print(f"Total semua angka: {total}")
    
    if total % 2 != 0:
        print("\nHasil: False")
        print("Alasan: Total angka ganjil, tidak bisa dibagi menjadi 2 bagian sama.")
        return False
    
    target = total // 2
    print(f"Target per bagian: {target}")
    
    n = len(daftar_angka)
    
    dp = [False] * (target + 1)
    dp[0] = True 
    
    for angka in daftar_angka:
        for i in range(target, angka - 1, -1):
            if dp[i - angka]:
                dp[i] = True
    
    hasil = dp[target]
    
    print(f"\nHasil: {hasil}")
    
    if hasil:
        print("List dapat dibagi menjadi 2 bagian dengan jumlah yang sama!")
        print(f"Setiap bagian berjumlah: {target}")
    else:
        print("List TIDAK dapat dibagi menjadi 2 bagian dengan jumlah yang sama.")
    
    return hasil

def main():
    daftar_angka = []
    
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (1-6): ")
        
        if pilihan == "1":
            tambah_angka(daftar_angka)
        elif pilihan == "2":
            tampilkan_list(daftar_angka)
        elif pilihan == "3":
            ubah_angka(daftar_angka)
        elif pilihan == "4":
            hapus_angka(daftar_angka)
        elif pilihan == "5":
            cek_pembagian_sama(daftar_angka)
        elif pilihan == "6":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid!")

if __name__ == "__main__":
    main()