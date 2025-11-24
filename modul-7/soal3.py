def tampil_menu():
    print("\n=== SISTEM KUPON ===")
    print("1. Tampilkan semua kupon")
    print("2. Tampilkan daftar barang")
    print("3. Tambah barang baru")
    print("4. Edit barang")
    print("5. Hapus barang")
    print("6. Proses transaksi (pilih barang + kupon)")
    print("7. Tambah kupon baru")
    print("8. Keluar")


def tampil_kupon(kupon_dict):
    if not kupon_dict:
        print("Tidak ada kupon tersedia.")
        return
    for kode, persen in kupon_dict.items():
        print(f"- {kode}: {persen}%")


def tampil_barang(barang_list):
    if not barang_list:
        print("Belum ada barang.")
        return

    for i, (nama, harga) in enumerate(barang_list, start=1):
        print(f"{i}. {nama} - Rp{harga}")


def tambah_barang(barang_list, nama, harga_str):
    try:
        harga = float(harga_str)
        if harga <= 0:
            print("Harga harus lebih dari 0.")
            return False
    except ValueError:
        print("Harga harus berupa angka.")
        return False

    barang_list.append((nama, harga))
    print(f"Barang '{nama}' ditambahkan dengan harga Rp{harga}.")
    return True


def edit_barang(barang_list, index_str, nama_baru, harga_str):
    try:
        index = int(index_str) - 1
        if index < 0 or index >= len(barang_list):
            print("Nomor barang tidak valid.")
            return False
    except ValueError:
        print("Nomor barang harus angka.")
        return False

    try:
        harga_baru = float(harga_str)
        if harga_baru <= 0:
            print("Harga harus lebih dari 0.")
            return False
    except ValueError:
        print("Harga harus berupa angka.")
        return False

    barang_list[index] = (nama_baru, harga_baru)
    print("Barang berhasil diperbarui!")
    return True


def hapus_barang(barang_list, index_str):
    try:
        index = int(index_str) - 1
        if index < 0 or index >= len(barang_list):
            print("Nomor barang tidak valid.")
            return False
    except ValueError:
        print("Nomor barang harus angka.")
        return False

    nama, _ = barang_list.pop(index)
    print(f"Barang '{nama}' telah dihapus.")
    return True


def proses_transaksi(kupon_dict, barang_list, index_str, kode):
    try:
        index = int(index_str) - 1
        if index < 0 or index >= len(barang_list):
            print("Nomor barang tidak valid.")
            return None
    except ValueError:
        print("Nomor barang harus angka.")
        return None

    nama_barang, harga = barang_list[index]

    persen = kupon_dict.get(kode)
    if persen is None:
        print("Kupon tidak valid atau sudah dipakai.")
        return None

    diskon = harga * (persen / 100.0)
    total_bayar = harga - diskon
    del kupon_dict[kode]

    print(f"\nBarang: {nama_barang}")
    print(f"Harga asli: Rp{harga}")
    print(f"Kupon {kode} ({persen}%) → Diskon: Rp{diskon:.2f}")
    print(f"Total bayar: Rp{total_bayar:.2f}")
    return total_bayar


def tambah_kupon(kupon_dict, kode, persen_str):
    if kode in kupon_dict:
        print("Kode kupon sudah ada.")
        return False

    try:
        persen = float(persen_str)
        if not (0 < persen <= 100):
            print("Persentase harus > 0 dan <= 100.")
            return False
    except ValueError:
        print("Persentase harus berupa angka.")
        return False

    kupon_dict[kode] = persen
    print(f"Kupon '{kode}' ditambahkan ({persen}%).")
    return True


def main():
    kupon_dict = {
        "WELCOME10": 10,
        "DISC20": 20
    }

    barang_list = []

    while True:
        tampil_menu()
        pilihan = input("Pilih menu (1-8): ").strip()

        if pilihan == "1":
            tampil_kupon(kupon_dict)

        elif pilihan == "2":
            tampil_barang(barang_list)

        elif pilihan == "3":
            nama = input("Nama barang: ").strip()
            harga = input("Harga barang: ").strip()
            tambah_barang(barang_list, nama, harga)

        elif pilihan == "4":
            tampil_barang(barang_list)
            nomor = input("Pilih nomor barang yg ingin diedit: ")
            nama_baru = input("Nama baru: ").strip()
            harga_baru = input("Harga baru: ").strip()
            edit_barang(barang_list, nomor, nama_baru, harga_baru)

        elif pilihan == "5":
            tampil_barang(barang_list)
            nomor = input("Nomor barang yg ingin dihapus: ")
            hapus_barang(barang_list, nomor)

        elif pilihan == "6":
            tampil_barang(barang_list)
            nomor = input("Pilih nomor barang: ")
            kode = input("Masukkan kode kupon: ").strip().upper()
            proses_transaksi(kupon_dict, barang_list, nomor, kode)

        elif pilihan == "7":
            kode = input("Kode kupon: ").strip().upper()
            while True:
                persen = input("Persen diskon: ").strip()
                if tambah_kupon(kupon_dict, kode, persen):
                    break
                else:
                    print("Input persen salah! Coba lagi.\n")

        elif pilihan == "8":
            print("Keluar.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()