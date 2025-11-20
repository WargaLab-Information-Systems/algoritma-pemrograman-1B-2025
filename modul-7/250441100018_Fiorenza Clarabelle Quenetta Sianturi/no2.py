inventaris = {}

def menu():
    while True:
        print("\nmenu manajemen Inventaris Gudang:")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan ID")
        print("3. Tambah barang baru")
        print("4. Perbarui stok barang")
        print("5. Hapus barang")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == '1':
            tampilkan()
        elif pilihan == '2':
            cari()
        elif pilihan == '3':
            tambah()
        elif pilihan == '4':
            perbarui()
        elif pilihan == '5':
            hapus()     
        elif pilihan == '6':
            print("program selesai")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.") 
        
def tampilkan():
    if not inventaris:
        print("belum ada barang")
    else:
        for barang, info in inventaris.items():
            print(f"ID: {barang}, Nama Barang: {info[0]}, Harga: {info[1]}, Stok: {info[2]}")
            
def cari():
    id = input("masukkan id/nama/harga/stok barang yang dicari: ")
    for barang, info in inventaris.items():
        if info[0] == id or info[1] == id or info[2] or barang == id :
            print(f"ID: {barang}, Nama Barang: {info[0]}, Harga: {info[1]}, Stok: {info[2]}")
        else:
            print(f"{id} tidak ditemukan")

def tambah():
    while True:
        nama = input("masukkan nama barang: ")
        if nama != " " and not nama.isalpha():
            print("nama tidak boleh kosong dan bukan huruf")
        else:
            print("nama barang berhasil ditambahkan")
            break
    while True:
        harga = input("masukkan harga barang: ")
        if harga == "" or not harga.isdigit():
            print("harga harus diatas 0 dan gak boleh kosong")
        else:
            harga_int = int(harga)
            if harga_int > 0:
                print("harga berhasil ditambahkan")
                break
            else:
                print("harga harus diatas 0 dan gak boleh kosong")
            
    while True:
        stok = input("masukkan stok barang(berupa angka): ")
        if stok == "" or not stok.isdigit():
            print("stok harus berupa angka positif dan gak boleh kosong")
        else:
            stok_int = int(stok)
            if stok_int > 0:
                print("stok berhasil ditambahkan")
                break
            else:
                print("stok harus berupa angka positif dan gak boleh kosong")

            
    while True:
        id = input("masukkan id barang: ")
        if id == "":
            print("id barang tidak boleh kosong")
            continue
        if not id.isalnum():
            print("id harus angka/huruf")
            continue
        if id in inventaris:
            print("id barang sudah ada")
            continue
        else:
            inventaris[id] = [nama, harga, stok]
            print(f"barang {nama} dengan id {id} berhasil ditambahkan")
            break
    
def perbarui():
    while True:
        id = input("masukkan id yang mau diperbarui: ")
        if id in inventaris:
            baru = int(input("masukkan stok baru:"))
            if baru <= 0:
                print("stok tidak boleh kosong/negatif")
                print()
            else:
                inventaris[id][2] = baru
                print("stok berhasil diperbarui")
                break
        else:
            print("id barang tidak ditemukan")
        
def hapus():
    id = input("masukkan id/nama/harga/stok barang yang mau dihapus: ")
    for hapus, info in inventaris.items():
        if info[0] == id or info[1] == id or info[2] or hapus == id :
            print(f"ID: {hapus}, Nama Barang: {info[0]}, Harga: {info[1]}, Stok: {info[2]}")
        else:
            print(f"{id} tidak ditemukan")
        
menu()