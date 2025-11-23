def proses_transaksi(kupon, total_belanja, kode_kupon):
    if kode_kupon in kupon:
        diskon = kupon[kode_kupon]
        total_diskon = (diskon / 100) * total_belanja
        total_setelah_diskon = total_belanja - total_diskon
        print(f"Kupon valid! Total belanja: {total_belanja}, Diskon: {total_diskon}, Total yang harus dibayar: {total_setelah_diskon}")
        del kupon[kode_kupon]
        print("Kupon telah digunakan dan dihapus.")
    else:
        print("Kupon tidak valid atau sudah digunakan.")
        
def tampilkan_kupon(kupon):
    if not kupon:
        print("Tidak ada kupon yang tersedia.")
    else:
        print("Kupon yang tersedia:")
        for kode, diskon in kupon.items():
            print(f"Kode: {kode}, Diskon: {diskon}%")

def menu(kupon):
    while True:
        print("\nMenu Kupon Diskon:")
        print("1. Proses transaksi")
        print("2. Tampilkan semua kupon")
        print("3. Keluar")
        
        pilihan = input("Pilih opsi (1-3): ")
        
        if pilihan == '1':
            total_belanja = float(input("Masukkan total belanja: "))
            kode_kupon = input("Masukkan kode kupon: ")
            proses_transaksi(kupon, total_belanja, kode_kupon)
        elif pilihan == '2':
            tampilkan_kupon(kupon)
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    kupon = {
        "DISKON10": 10,
        "DISKON20": 20,
        "DISKON30": 30
    }
    menu(kupon)