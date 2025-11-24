def tampil_menu():
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambah barang baru")
    print("4. Perbarui stok barang")
    print("5. Hapus barang")
    print("6. Keluar")

def validasi_id(id_item):
    if not id_item.isdigit():
        print("ID hanya boleh berisi angka.")
        return False
    return True

def tampil_semua(inventaris):
    if not inventaris:
        print("Tidak ada barang di inventaris.")
        return
    for id_item, info in inventaris.items():
        print(f"- ID {id_item}: Nama={info[0]}, Harga={info[1]}, Stok={info[2]}")

def cari_barang(inventaris, id_item):
    info = inventaris.get(id_item)
    if info:
        print(f"ID {id_item}: Nama={info[0]}, Harga={info[1]}, Stok={info[2]}")
    else:
        print(f"Barang dengan ID '{id_item}' tidak ditemukan.")

def tambah_barang(inventaris, id_item, nama, harga, stok):
    if id_item in inventaris:
        print(f"ID '{id_item}' sudah ada.")
        return False
    try:
        harga = float(harga)
        if harga <= 0:
            print("Harga tidak boleh 0 atau negatif.")
            return False

        stok = int(stok)
        if stok <= 0:
            print("Stok tidak boleh 0 atau negatif.")
            return False
    except ValueError:
        print("Harga harus angka dan stok harus integer.")
        return False

    inventaris[id_item] = [nama, harga, stok]
    print(f"Barang '{nama}' (ID {id_item}) ditambahkan.")
    return True

def update_stok(inventaris, id_item, delta):
    if id_item not in inventaris:
        print(f"Barang dengan ID '{id_item}' tidak ditemukan.")
        return False
    try:
        delta = int(delta)
    except ValueError:
        print("Perubahan stok harus berupa angka integer (positif/negatif).")
        return False
    new_stok = inventaris[id_item][2] + delta
    if new_stok < 0:
        print("Operasi dibatalkan: stok tidak boleh menjadi negatif.")
        return False
    inventaris[id_item][2] = new_stok
    print(f"Stok ID {id_item} diperbarui menjadi {new_stok}.")
    return True

def hapus_barang(inventaris, id_item):
    if id_item in inventaris:
        del inventaris[id_item]
        print(f"Barang ID {id_item} dihapus.")
        return True
    else:
        print(f"Barang dengan ID '{id_item}' tidak ditemukan.")
        return False

def main():
    inventaris = {}

    while True:
        tampil_menu()
        pilihan = input("Pilih (1-6): ").strip()

        if pilihan == "1":
            tampil_semua(inventaris)

        elif pilihan == "2":
            id_item = input("Masukkan ID barang: ").strip()
            cari_barang(inventaris, id_item)

        elif pilihan == "3":
            while True:
                id_item = input("ID: ").strip()

                if not validasi_id(id_item):
                    continue

                if id_item in inventaris:
                    print("ID sudah ada, gunakan ID lain.")
                else:
                    break

            while True:
                nama = input("Nama barang: ").strip()
                if any(c.isdigit() for c in nama):
                    print("Nama tidak boleh mengandung angka.")
                elif nama == "":
                    print("Nama tidak boleh kosong.")
                else:
                    break

            while True:
                harga = input("Harga: ").strip()
                try:
                    harga_val = float(harga)
                    if harga_val <= 0:
                        print("Harga tidak boleh 0 atau negatif.")
                    else:
                        break
                except ValueError:
                    print("Harga harus berupa angka.")

            while True:
                stok = input("Stok: ").strip()
                try:
                    stok_val = int(stok)
                    if stok_val <= 0:
                        print("Stok tidak boleh 0 atau negatif.")
                    else:
                        break
                except ValueError:
                    print("Stok harus berupa angka integer.")

            inventaris[id_item] = [nama, harga_val, stok_val]
            print(f"Barang '{nama}' (ID {id_item}) ditambahkan.")

        elif pilihan == "4":
            id_item = input("ID barang: ").strip()
            delta = input("Perubahan stok (mis. 5 atau -3): ").strip()
            update_stok(inventaris, id_item, delta)

        elif pilihan == "5":
            id_item = input("ID barang yang ingin dihapus: ").strip()
            hapus_barang(inventaris, id_item)

        elif pilihan == "6":
            print("Keluar. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()