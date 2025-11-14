




angka = []

def tambah_angka():
    nilai = int(input("Masukkan angka: "))
    angka.append(nilai)
    print("Angka berhasil ditambahkan!")

def tampilkan_angka():
    print("Daftar angka saat ini:", angka)

def ubah_angka():
    index = int(input("Index yang ingin diubah: "))
    if 0 <= index < len(angka):
        nilai_baru = int(input("Masukkan nilai baru: "))
        angka[index] = nilai_baru
        print("Data berhasil diupdate!")
    else:
        print("Index tidak valid!")

def hapus_angka():
    nilai = int(input("Nilai yang ingin dihapus: "))
    if nilai in angka:
        angka.remove(nilai)
        print("Data berhasil dihapus!")
    else:
        print("Nilai tidak ditemukan!")

def cek_pembagian_sama():
    total = 0
    for x in angka:
        total = total + x
    if total % 2 == 1:
        print(False)
    else:
        target = total // 2
        jumlah = 0
        print("benar =", target)
        ketemu = True
        for x in angka:
            jumlah = jumlah + x
            if jumlah == target:
                ketemu = True
                break
        print(ketemu)

while True:
    print("\n=== MENU ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Apakah Bisa Dibagi Dua Sama Jumlah")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_angka()
    elif pilih == "2":
        tampilkan_angka()
    elif pilih == "3":
        ubah_angka()
    elif pilih == "4":
        hapus_angka()
    elif pilih == "5":
        cek_pembagian_sama()
    elif pilih == "6":
        break
    else:
        print("Pilihan tidak valid!")
