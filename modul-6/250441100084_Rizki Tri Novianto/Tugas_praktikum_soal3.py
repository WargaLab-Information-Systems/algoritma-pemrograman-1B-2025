data = []

def tambah_angka():
    angka = int(input("Masukkan angka yang ingin ditambahkan: "))
    data.append(angka)
    print("Angka berhasil ditambahkan.")

def tampilkan_data():
    print("Isi data saat ini:", data)

def ubah_angka():
    indeks = int(input("Masukkan indeks yang ingin diubah: "))
    #len di gunakan agar saat mengecek indeks tidak melebihi panjang dari list
    if 0 <= indeks < len(data):
        angka_baru = int(input("Masukkan angka baru: "))
        data[indeks] = angka_baru
        print("Data berhasil diubah.")
    else:
        print("Indeks tidak valid.")

def hapus_angka():
    indeks = int(input("Masukkan indeks yang ingin dihapus: "))
    if 0 <= indeks < len(data):
        del data[indeks]
        print("Data berhasil dihapus.")
    else:
        print("Indeks tidak valid.")

def cek_pembagian():
    total = sum(data) 
    if total % 2 != 0:
        print("False (jumlah total ganjil, tidak bisa dibagi dua sama rata)")
        return

    target = total // 2
    jumlah = 0
    for angka in data:
        jumlah += angka
        if jumlah == target:
            print("True (bisa dibagi dua bagian dengan jumlah sama)")
            return
    print("False (tidak ditemukan pembagian yang seimbang)")

# Menu utama
while True:
    print("\n=== Program Pembagian Deretan Angka ===")
    print("1. Tambah angka")
    print("2. Tampilkan data")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek pembagian")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_angka()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        ubah_angka()
    elif pilihan == "4":
        hapus_angka()
    elif pilihan == "5":
        cek_pembagian()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
