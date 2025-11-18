data = []  # List utama

def cek_pembagian_sama(data):
    total = sum(data)
    # Jika total tidak genap, langsung tidak bisa dibagi
    if total % 2 != 0:
        return None  # Tidak bisa dibagi dua sama besar
    
    target = total // 2
    jumlah_sementara = 0
    bagian_kiri = []

    # Coba cari titik pembagian
    for angka in data:
        jumlah_sementara += angka
        bagian_kiri.append(angka)
        if jumlah_sementara == target:
            # Bagian kiri dan kanan ditemukan
            bagian_kanan = data[len(bagian_kiri):]
            return (bagian_kiri, bagian_kanan)
    
    return None  # Tidak ditemukan titik pembagian


while True:
    print("\n=== PROGRAM DERET ANGKA (CRUD) ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Pembagian Dua Bagian Sama Nilai")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah angka yang ingin ditambah: "))
        for i in range(jumlah):
            angka = int(input(f"Masukkan angka ke-{i+1}: "))
            data.append(angka)
        print(f"{jumlah} angka berhasil ditambahkan:", data)

    elif pilihan == "2":
        print("Daftar angka:", data)

    elif pilihan == "3":
        if data:
            indeks = int(input("Masukkan index yang ingin diubah: "))
            if 0 <= indeks < len(data):
                angka_baru = int(input("Masukkan angka baru: "))
                data[indeks] = angka_baru
                print("Data berhasil diubah.")
            else:
                print("Index tidak valid.")
        else:
            print("Data masih kosong.")

    elif pilihan == "4":
        if data:
            indeks = int(input("Masukkan index yang ingin dihapus: "))
            if 0 <= indeks < len(data):
                data.pop(indeks)
                print("Data berhasil dihapus.")
            else:
                print("Index tidak valid.")
        else:
            print("Data masih kosong.")

    elif pilihan == "5":
        hasil = cek_pembagian_sama(data)
        if hasil:
            kiri, kanan = hasil
            print("True — Deret dapat dibagi menjadi dua bagian dengan jumlah sama.")
            print(f"Bagian kiri: {kiri}  → jumlah = {sum(kiri)}")
            print(f"Bagian kanan: {kanan}  → jumlah = {sum(kanan)}")
        else:
            print("False — Tidak ada pembagian dengan jumlah sama.")

    elif pilihan == "6":
        print("Program selesai. Terima kasih.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
