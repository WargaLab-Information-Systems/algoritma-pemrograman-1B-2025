
contacts = {} 
next_id = 1 
def tampilkan_semua(): 
    if not contacts: 
        print("Belum ada kontak.") 
        return 
    print("Daftar Kontak:") 
 
    daftar_id = [] 
    for nama, info in contacts.items(): 
        daftar_id.append((info[0], nama)) 
 
    daftar_id = sorted(daftar_id) 
    for id_kontak, nama in daftar_id: 
        telp = contacts[nama][1] 
        email = contacts[nama][2] 
        print(f"Nama: {nama} | ID: {id_kontak} -> Telp: {telp}, Email: {email}") 
 
def cari_kontak(): 
    nama = input("Masukkan nama yang dicari: ") 
    if nama in contacts: 
        info = contacts[nama] 
        print(f"{nama} ditemukan.") 
        print(f"ID: {info[0]}, Telp: {info[1]}, Email: {info[2]}") 
    else: 
        print("Kontak tidak ditemukan.") 
 
def tambah_kontak(): 
    global next_id 
 
    nama = input("Nama: ") 
    if not nama.isalpha(): 
        print("Nama harus menggunakan huruf! Kontak tidak disimpan.") 
        return 
    if nama in contacts: 
        print("Nama sudah ada di kontak. Gunakan nama lain atau update kontak yang ada.") 
        return 
    telp = input("No Telepon: ") 
    if not telp.isdigit(): 
        print("Nomor telepon harus berupa angka! Kontak tidak disimpan.") 
        return 
    email = input("Email: ") 
    if "@" not in email : 
        print("Email tidak valid (harus mengandung '@' )! Kontak tidak disimpan.") 
        return 
    new_id = next_id 
    contacts[nama] = [new_id, telp, email] 
    next_id += 1 
    print(f"Kontak berhasil ditambahkan. ID = {new_id}") 
 
def update_email(): 
    daftar_id = [] 
    for nama, info in contacts.items(): 
        daftar_id.append((info[0], nama)) 
 
    daftar_id = sorted(daftar_id) 
    if not contacts: 
        print("Belum ada kontak.") 
    else: 
        print("Daftar Kontak:") 
        for nama, info in contacts.items(): 
            print(f"Nama: {nama} | ID: {info[0]} -> Telp: {info[1]}, Email: {info[2]}") 
 
    nama = input("Masukkan nama kontak yang akan diupdate: ") 
    if nama in contacts: 
        email_baru = input("Email baru: ") 
        if "@" not in email_baru: 
            print("Email tidak valid. Perubahan dibatalkan.") 
            return 
        contacts[nama][2] = email_baru 
        print("Email berhasil diperbarui.") 
    else: 
        print("Kontak tidak ditemukan.") 
 
def reindex(): 
    data = [] 
    for nama, info in contacts.items(): 
        data.append((info[0], nama, info[1], info[2])) 

    data = sorted(data) 
    contacts.clear() 
    new_id = 1 

    for _, nama, telp, email in data: 
        contacts[nama] = [new_id, telp, email] 
        new_id += 1 
 
    global next_id 
    next_id = new_id 
 
def hapus_kontak(): 
    daftar_id = [] 
    for nama, info in contacts.items(): 
        daftar_id.append((info[0], nama)) 
 
    daftar_id = sorted(daftar_id) 
 
    for id_kontak, nama in daftar_id: 
        telp = contacts[nama][1] 
        email = contacts[nama][2] 
        print(f"Nama: {nama} | ID: {id_kontak} -> Telp: {telp}, Email: {email}") 
    if not contacts: 
        print("Belum ada kontak.") 
        return 
 
    nama = input("Masukkan nama yang akan dihapus: ") 
    if nama in contacts: 
        del contacts[nama] 
        print("Kontak berhasil dihapus.") 
        reindex() 
    else: 
        print("Kontak tidak ditemukan.") 
 
while True: 
    print("=== CONTACT BOOK ===") 
    print("1. Tampilkan Semua Kontak") 
    print("2. Cari Kontak") 
    print("3. Tambah Kontak") 
    print("4. Update Email") 
    print("5. Hapus Kontak") 
    print("6. Keluar") 
 
    pilihan = input("Pilih menu: ") 
 
    if pilihan == "1": 
        tampilkan_semua() 
    elif pilihan == "2": 
        cari_kontak() 
    elif pilihan == "3":
         tambah_kontak() 
    elif pilihan == "4": 
        update_email() 
    elif pilihan == "5": 
        hapus_kontak() 
    elif pilihan == "6": 
        print("Keluar dari program.") 
        break 
    else: 
        print("Pilihan tidak valid.")