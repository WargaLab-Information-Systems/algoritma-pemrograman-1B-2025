angka = [] 
def cek_sama(angka):
    n = len(angka)
    if n % 2 != 0: 
        return False
    tengah = n // 2
    kiri = 0
    kanan = 0
    for i in range(tengah):
        kiri += angka[i]
    for i in range(tengah, n):
        kanan += angka[i]
    return kiri == kanan

# Menu CRUD
while True:
    print("\n=== MENU DOMINIC SZOBOSZLAI ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Pembagian Sama Besar")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        nilai = int(input("Masukkan angka: "))
        angka.append(nilai)
        print("Angka berhasil ditambahkan.")

    elif pilih == "2":
        print("Daftar angka:", angka)

    elif pilih == "3":
        if not angka:
            print("List masih kosong!")
        else:
            print("Daftar angka:", angka)
            idx = int(input("Masukkan indeks yang ingin diubah: "))
            if 0 <= idx < len(angka):
                angka[idx] = int(input("Masukkan angka baru: "))
                print("Data berhasil diubah.")
            else:
                print("Indeks tidak valid!")

    elif pilih == "4":
        if not angka:
            print("List masih kosong!")
        else:
            print("Daftar angka:", angka)
            idx = int(input("Masukkan indeks yang ingin dihapus: "))
            if 0 <= idx < len(angka):
                del angka[idx]
                print("Data berhasil dihapus.")
            else:
                print("Indeks tidak valid!")

    elif pilih == "5":
        if len(angka) < 2:
            print("Data terlalu sedikit untuk dicek.")
        else:
            hasil = cek_sama(angka)
            print("Hasil:", hasil)

    elif pilih == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")