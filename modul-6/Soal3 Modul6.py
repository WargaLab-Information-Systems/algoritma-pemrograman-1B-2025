angka = []

def tambah_angka():
    try:
        n = int(input("Masukkan angka yang ingin ditambah: "))
        angka.append(n)
        print("Angka berhasil ditambahkan.\n")
    except ValueError:
        print("Input harus berupa angka!\n")

def tampilkan_angka():
    if len(angka) == 0:
        print("Belum ada angka dalam daftar.\n")
    else:
        print("Daftar angka saat ini:", angka, "\n")

def ubah_angka():
    if len(angka) == 0:
        print("Belum ada angka untuk diubah.\n")
        return
    
    try:
        indeks = int(input("Masukkan indeks yang ingin diubah: "))
        if 0 <= indeks < len(angka):
            nilai_baru = int(input("Masukkan nilai baru: "))
            angka[indeks] = nilai_baru
            print("Angka berhasil diubah.\n")
        else:
            print("Indeks tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka!\n")

def hapus_angka():
    if len(angka) == 0:
        print("Belum ada angka untuk dihapus.\n")
        return
    
    try:
        indeks = int(input("Masukkan indeks yang ingin dihapus: "))
        if 0 <= indeks < len(angka):
            baru = []
            # Salin semua elemen kecuali indeks yang dihapus
            for i in range(len(angka)):
                if i != indeks:
                    baru += [angka[i]]
            # Ganti isi list lama dengan list baru
            angka.clear()
            for item in baru:
                angka.append(item)
            print("Angka berhasil dihapus.\n")
        else:
            print("Indeks tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka!\n")

def cek_pembagian():
    if len(angka) == 0:
        print("Belum ada angka untuk dicek.\n")
        return

    # Hitung total manual
    total = 0
    for i in angka:
        total += i

    # Jika total ganjil, otomatis tidak bisa dibagi sama rata
    if total % 2 != 0:
        print("False — tidak bisa dibagi dua bagian dengan jumlah yang sama.\n")
        return

    setengah = total // 2
    jumlah = 0
    for i in angka:
        jumlah += i
        if jumlah == setengah:
            print("True — dapat dibagi menjadi dua bagian dengan jumlah yang sama.\n")
            return

    print("False — tidak bisa dibagi dua bagian yang seimbang.\n")


# === Program Utama ===
while True:
    print("=== Program Deretan Angka Szoboszlai ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Pembagian Dua Bagian")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_angka()
    elif pilihan == '2':
        tampilkan_angka()
    elif pilihan == '3':
        ubah_angka()
    elif pilihan == '4':
        hapus_angka()
    elif pilihan == '5':
        cek_pembagian()
    elif pilihan == '6':
        print("Program selesai. Terima kasih!\n")
        break
    else:
        print("Pilihan tidak valid.\n")