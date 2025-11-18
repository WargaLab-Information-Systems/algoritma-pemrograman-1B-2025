pengunjung = []

def tambah(pengunjung):
    id_antrian = len(pengunjung) + 1       #Menghitung ID antrian berdasarkan jumlah data yg ada.
    nama_pengunjung = input("nama pengunjung: ")
    nama_santri = input("nama santri yang dijenguk: ")
    daerah_asal = input("daerah asal pengunjung (sumatra, kalimantan, atau jawa): ")
    
    pengunjung.append([id_antrian, nama_pengunjung, nama_santri, daerah_asal])      #ini untuk Menyimpan semua data tadi ke dlm list pengunjung dlm bentuk sublist.
    print(f"ID antrian: {id_antrian}")
    print(f"nama pengunjung: {nama_pengunjung}")
    print(f"nama santri: {nama_santri}")
    print(f"daerah asal: {daerah_asal}")

def tampilkan_list(pengunjung):     #Membuat fungsi untuk menampilkan daftar pengunjung berdasarkan asal daerah.
    asal = {"sumatra": [], "kalimantan": [], "jawa": []}    #ini dictionary
    
    for pengunjung in pengunjung:       #melakukan perulangan data dilist pengunjung trs masukin kekelompok asal
        asal[pengunjung[3]].append(pengunjung)

    for daerah in ["sumatra", "kalimantan", "jawa"]:       #looping 3x tiap daerah
        if asal[daerah]:        #cek dari daerah itu apa tdk
            print(f"Pengunjung dari {daerah}:")
            for pengunjung in asal[daerah]:     #nampilin data pengunjung dr daerah tsb,id,nama,santri
                print(f"id {pengunjung[0]}, nama pengunjung: {pengunjung[1]}, nama santri yang di jenguk: {pengunjung[2]}")
        
def hapus(pengunjung):
    id_input = input("masukan ID Antrian yang ingin dihapus: ")
    id_antrian = int(id_input)
    for item in pengunjung:     #cek tiap data dilist, idnya sm ap tdk 
        if item[0] == id_antrian:
            pengunjung.remove(item)
            print(f"Data kunjungan dengan ID Antrian {id_antrian} berhasil dihapus.")
            break
    else:
        print("ID antrian tidak ditemukan.")


def menu():     #buat fungsi utama biar pengguna bs memilih tindakan
    while True:
        print("\n=====sistem kunjungan santri=====")
        print("1. tambah pengunjung")
        print("2. menampilkan daftar pengunjung")
        print("3. hapus pengunjung")
        print("4. keluar")
        pilihan = input("silahkan pilih (1-4): ")
        print()
        if pilihan == "1":
            tambah(pengunjung)
        elif pilihan == "2":
            tampilkan_list(pengunjung)
        elif pilihan == "3":
            hapus(pengunjung)
        elif pilihan == "4":
            print("sistem selesai")
            break
        else:
            print("silahkan pilih dari 1-4")

menu()


