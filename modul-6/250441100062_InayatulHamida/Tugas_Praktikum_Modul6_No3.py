def tampilkan_menu():
    print("\nMenu:")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Pembagian Angka")
    print("6. Keluar")

def tambah_angka(daftar_angka):
    angka = int(input("Masukkan angka yang ingin ditambahkan: "))
    daftar_angka.append(angka)
    print(f"Angka {angka} berhasil ditambahkan.")

def tampilkan_angka(daftar_angka):
    print("Daftar Angka:", daftar_angka)

def ubah_angka(daftar_angka):
    index = int(input("Masukkan index angka yang ingin diubah: "))    
    if 0 <= index < len(daftar_angka):
        angka_baru = int(input("Masukkan angka baru: "))
        daftar_angka[index] = angka_baru
        print(f"Angka di index {index} berhasil diubah menjadi {angka_baru}.")
    else:
        print("Index tidak valid.")

def hapus_angka(daftar_angka):
    index = int(input("Masukkan index angka yang ingin dihapus: "))
    if 0 <= index < len(daftar_angka):
        removed = daftar_angka.pop(index)
        print(f"Angka {removed} di index {index} berhasil dihapus.")
    else:
        print("Index tidak valid.")

def cek_pembagian(daftar_angka):
    if len(daftar_angka) % 2 == 0 and len(daftar_angka) > 0:
        tengah = len(daftar_angka)//2
        kiri, kanan = daftar_angka[:tengah], daftar_angka[tengah:]
        print("bagian 1:", kiri)
        print("bagian 2:", kanan)
        print("hasil:", sum(kiri) == sum(kanan))
    else:
        print("jumlah elemen harus genap dan tidak kosong!")

def menu():
    daftar_angka = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tambah_angka(daftar_angka)
        elif pilihan == '2':
            tampilkan_angka(daftar_angka)
        elif pilihan == '3':
            ubah_angka(daftar_angka)
        elif pilihan == '4':
            hapus_angka(daftar_angka)
        elif pilihan == '5':
            cek_pembagian(daftar_angka)
        elif pilihan == '6':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

menu()