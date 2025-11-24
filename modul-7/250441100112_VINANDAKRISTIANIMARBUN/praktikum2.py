


inventaris = {} 
next_id = 1 
 
def tampilkan_semua(): 
    if not inventaris: 
        print("Belum ada barang dalam inventaris.") 
    else: 
        print("Daftar Barang (urut berdasarkan ID):") 
 
    for id_brg in sorted(inventaris.keys()): 
        nama, harga, stok = inventaris[id_brg] 
        print(f"ID: {id_brg} | Nama Barang : {nama} | Harga: {harga} | Stok: {stok}") 
 
def cari_barang(): 
    id_brg = input("Masukkan ID barang: ") 
    if not id_brg.isdigit(): 
        print("ID harus berupa angka.") 
        return 
    id_brg = int(id_brg) 
 
    if id_brg in inventaris: 
        nama, harga, stok = inventaris[id_brg] 
        print(f"ID: {id_brg} -> Nama: {nama}, Harga: {harga}, Stok: {stok}") 
    else: 
        print("Barang tidak ditemukan.") 
 
def get_available_id(): 
    id_now = 1 
    while id_now in inventaris: 
        id_now += 1 
    return id_now 
 
def tambah_barang(): 
    nama = input("Nama Barang: ") 
    if not nama: 
        print("Nama barang tidak boleh kosong.") 
        return 
 
    harga_input = input("Harga: ") 
    if not harga_input.isdigit(): 
        print("Harga harus berupa angka.") 
        return 
 
    stok_input = input("Stok: ") 
    if not stok_input.isdigit(): 
        print("Stok harus berupa bilangan bulat.") 
        return 
 
    stok = int(stok_input) 
 
    new_id = get_available_id() 
    inventaris[new_id] = [nama, harga_input, stok] 
    print(f"Barang berhasil ditambahkan. ID = {new_id}") 
 
def update_stok(): 
    for id_brg in sorted(inventaris.keys()): 
        nama, harga, stok = inventaris[id_brg] 
        print(f"ID: {id_brg} | Nama Barang : {nama} | Harga: {harga} | Stok: {stok}") 
 
    if not inventaris: 
        print("Belum ada barang.") 
        return 
 
    id_input = input("Masukkan ID barang yang akan diupdate stoknya: ") 
    if not id_input.isdigit(): 
        print("ID harus berupa angka.") 
        return 
    id_brg = int(id_input) 
    if id_brg not in inventaris: 
        print("Barang tidak ditemukan.") 
        return 
    perubahan_input = input("Masukkan perubahan stok (+) : ") 
 
    if not perubahan_input.isdigit(): 
        print("Perubahan stok harus berupa angka.") 
        return 
     
    perubahan = int(perubahan_input) 
    nama, harga, stok_sekarang = inventaris[id_brg] 
 
    stok_baru = stok_sekarang + perubahan 
    inventaris[id_brg][2] = stok_baru 
 
    print(f"Stok untuk ID {id_brg} ({nama}) berhasil diperbarui: {stok_sekarang} -> {stok_baru}") 
 
def reindex_id(): 
    global inventaris 
    new_inventaris = {} 
    new_id = 1 
 
    for old_id in sorted(inventaris.keys()): 
        new_inventaris[new_id] = inventaris[old_id] 
        new_id += 1 
 
    inventaris = new_inventaris 
 
def hapus_barang(): 
    for id_brg in sorted(inventaris.keys()): 
        nama, harga, stok = inventaris[id_brg] 
        print(f"ID: {id_brg} | Nama Barang : {nama} | Harga: {harga} | Stok: {stok}") 
 
    id_input = input("Masukkan ID barang yang akan dihapus: ") 
    if not id_input.isdigit(): 
        print("ID harus berupa angka.") 
        return 
    id_brg = int(id_input) 
 
    if id_brg in inventaris: 
        del inventaris[id_brg] 
        reindex_id() 
        print(f"Barang dengan ID {id_brg} berhasil dihapus dan ID otomatis disusun ulang.") 
    else: 
        print("Barang tidak ditemukan.") 
 
 
 
while True: 
    print("=== INVENTARIS GUDANG ===") 
    print("1. Tampilkan Semua Barang") 
    print("2. Cari Barang (by ID)") 
    print("3. Tambah Barang") 
    print("4. Update Stok") 
    print("5. Hapus Barang") 
    print("6. Keluar") 
 
    pilihan = input("Pilih menu: ") 
 
    if pilihan == "1": 
        tampilkan_semua() 
    elif pilihan == "2": 
        cari_barang() 
    elif pilihan == "3": 
        tambah_barang() 
    elif pilihan == "4": 
        update_stok() 
    elif pilihan == "5": 
        hapus_barang() 
    elif pilihan == "6": 
        print("Keluar dari program.") 
        break 
    else: 
        print("Pilihan tidak valid.")