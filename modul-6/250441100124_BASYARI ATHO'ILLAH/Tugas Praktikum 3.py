data = []

def create():
    i = 1
    while True:
        angka_input = input(f"Masukkan angka ke-{i}: ")
        if not angka_input.isdigit():
            print("Program berhenti, semua angka masuk ke data.")
            break
        angka = int(angka_input)
        data.append(angka)
        i += 1


def read():
    if not data:
        print(" Tidak ada data angka.")
    else:
        print("Angka saat ini:", data)

def update():
    read() 
    if data:
        while True:
            try:
                indeks = int(input("Masukkan indeks angka yang ingin diubah: "))
                if 0 <= indeks < len(data):
                    angka_baru = int(input("Masukkan angka baru: "))
                    lama = data[indeks]
                    data[indeks] = angka_baru  
                    print(f"Angka {lama} telah diubah menjadi {angka_baru}")
                else:
                    print("Indeks tidak valid!")

                update_lagi = input("Apakah ada indeks lain yang perlu diubah? (y/n): ").lower()
                if update_lagi == "n":
                    print("Selesai mengubah data.")
                    break

            except ValueError:
                print("Masukkan angka yang valid!")

def delete():
    read()
    if data:
        try:
            indeks = int(input("Masukkan indeks angka yang ingin dihapus: "))
            if 0 <= indeks < len(data):
                angka = data.pop(indeks)
                print(f"Angka {angka} telah dihapus.")
            else:
                print("Indeks tidak valid!")
        except ValueError:
            print("Masukkan angka yang valid!")

def dua_bagian():
    if len(data) == 0:
        print("=== Cek Bagian ===")
        print("List masih kosong, tidak bisa dicek.")
        return
    
    if len(data) % 2 != 0:
        print("Jumlah elemen ganjil, tidak bisa dibagi dua bagian sama besar.")
        print("Hasil: False") 
        return

    tengah = len(data) // 2
    kiri = data[:tengah]
    kanan = data[tengah:]

    jumlah_kiri = sum(kiri)
    jumlah_kanan = sum(kanan) 

    print(f"angka kiri  : {kiri} = {jumlah_kiri}")
    print(f"angka kanan: {kanan} = {jumlah_kanan}")

    if jumlah_kiri == jumlah_kanan:
        print("Hasil: True")
    else:
        print("Hasil: False")

while True:
        print("\n=== Menu Angka Dominic  ===")
        print("1. Tambah Angka")
        print("2. Tampilkan data Angka")
        print("3. Ubah Angka")
        print("4. Hapus Angka")
        print("5. Cek Apakah bisa Dibagi Dua bagian")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            create()
        elif pilihan == "2":
            read()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            delete()
        elif pilihan == "5":
            dua_bagian()
        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")
 