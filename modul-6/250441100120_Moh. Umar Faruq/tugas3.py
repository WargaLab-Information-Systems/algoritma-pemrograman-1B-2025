# Program CRUD tanpa index untuk memeriksa apakah list dapat dibagi menjadi dua bagian dengan jumlah sama
data_angka = []

def create_data():
    n = int(input("Masukkan jumlah angka yang ingin ditambahkan: "))
    for i in range(n):
        angka = int(input(f"Masukkan angka ke-{i+1}: "))
        data_angka.append(angka)
    print("Data berhasil ditambahkan!")

def read_data():
    if not data_angka:
        print("Data masih kosong.")
    else:
        print("Daftar angka saat ini:", data_angka)

def update_data():
    if not data_angka:
        print("Data masih kosong, tidak bisa diubah.")
        return
    read_data()
    lama = int(input("Masukkan angka yang ingin diubah: "))
    if lama in data_angka:
        baru = int(input("Masukkan angka pengganti: "))
        
        hasil = []
        for x in data_angka:
            if x == lama and lama not in hasil: 
                hasil.append(baru)
                lama = None 
            else:
                hasil.append(x)
        data_angka.clear()
        for x in hasil:
            data_angka.append(x)
        print("Data berhasil diubah!")
    else:
        print("Angka tidak ditemukan dalam data!")

def delete_data():
    if not data_angka:
        print("Data masih kosong, tidak bisa dihapus.")
        return
    read_data()
    hapus = int(input("Masukkan angka yang ingin dihapus: "))
    if hapus in data_angka:
        hasil = []
        sudah_hapus = False
        for x in data_angka:
            if x == hapus and not sudah_hapus:
                sudah_hapus = True  
                continue
            hasil.append(x)
        data_angka.clear()
        for x in hasil:
            data_angka.append(x)
        print("Data berhasil dihapus!")
    else:
        print("Angka tidak ditemukan dalam data!")

def cek_pembagian_sama():
    if not data_angka:
        print("Data masih kosong, tidak bisa diperiksa.")
        return

    panjang = 0
    for _ in data_angka:
        panjang += 1

    if panjang % 2 != 0:
        print("False (jumlah elemen ganjil, tidak bisa dibagi dua sama besar)")
        return

    tengah = panjang // 2

    bagian1 = []
    bagian2 = []
    hitung = 0
    for angka in data_angka:
        if hitung < tengah:
            bagian1.append(angka)
        else:
            bagian2.append(angka)
        hitung += 1

    total1 = 0
    total2 = 0
    for a in bagian1:
        total1 += a
    for b in bagian2:
        total2 += b

    print(f"Bagian 1: {bagian1}, jumlah = {total1}")
    print(f"Bagian 2: {bagian2}, jumlah = {total2}")

    if total1 == total2:
        print("True (kedua bagian memiliki jumlah yang sama)")
    else:
        print("False (kedua bagian memiliki jumlah berbeda)")

while True:
    print("\n=== PROGRAM PEMERIKSAAN LIST DOMINIC ===")
    print("1. Tambah Data (Create)")
    print("2. Tampilkan Data (Read)")
    print("3. Ubah Data (Update)")
    print("4. Hapus Data (Delete)")
    print("5. Cek Pembagian Dua Bagian Sama")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        create_data()
    elif pilihan == "2":
        read_data()
    elif pilihan == "3":
        update_data()
    elif pilihan == "4":
        delete_data()
    elif pilihan == "5":
        cek_pembagian_sama()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        
