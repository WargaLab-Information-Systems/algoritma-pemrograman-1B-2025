def tampil_menu():
    print("\n=== CONTACT BOOK ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak (nama / email / telepon)")
    print("3. Tambah kontak baru")
    print("4. Perbarui email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

def validasi_nama(nama):
    if any(c.isdigit() for c in nama):
        print("Nama tidak boleh diisi angka.")
        return False
    return all(c.isalpha() or c.isspace() for c in nama)

def validasi_telepon(telepon):
    if not telepon.isdigit():
        print("Nomor telepon harus angka (tidak boleh huruf).")
        return False
    if len(telepon) < 12:
        print("Nomor telepon minimal harus 12 digit.")
        return False
    return True

def validasi_email(email):
    return "@" in email and "." in email

def input_nama():
    while True:
        nama = input("Nama: ").strip()
        if validasi_nama(nama):
            return nama

def tampil_semua(kontak):
    if not kontak:
        print("Tidak ada kontak.")
        return
    for nama, info in kontak.items():
        print(f"- {nama}: Telepon={info[0]}, Email={info[1]}")

def cari_kontak(kontak, keyword):
    hasil = []

    for nama, info in kontak.items():
        telepon, email = info

        if (keyword.lower() == nama.lower() or
            keyword == telepon or
            keyword.lower() == email.lower()):
            hasil.append((nama, telepon, email))

    if hasil:
        print("\nHasil pencarian:")
        for h in hasil:
            print(f"{h[0]}: Telepon={h[1]}, Email={h[2]}")
    else:
        print(f"Tidak ditemukan kontak dengan kata kunci '{keyword}'.")

def tambah_kontak(kontak, nama, telepon, email):
    for data in kontak.values():
        if data[1] == email:
            print("Email sudah digunakan. Harus berbeda.")
            return False

    original = nama
    counter = 1
    while nama in kontak:
        nama = f"{original} ({counter})"
        counter += 1

    kontak[nama] = [telepon, email]
    print(f"Kontak '{nama}' ditambahkan.")
    return True

def update_email(kontak, nama, email_baru):
    if nama not in kontak:
        print(f"Kontak '{nama}' tidak ditemukan.")
        return False

    if not validasi_email(email_baru):
        print("Format email tidak valid.")
        return False

    if kontak[nama][1] == email_baru:
        print("Email baru tidak boleh sama dengan email lama.")
        return False

    for key, data in kontak.items():
        if key != nama and data[1] == email_baru:
            print("Email sudah digunakan oleh kontak lain.")
            return False

    kontak[nama][1] = email_baru
    print(f"Email untuk '{nama}' diperbarui.")
    return True


def hapus_kontak(kontak, nama):
    if nama in kontak:
        del kontak[nama]
        print(f"Kontak '{nama}' dihapus.")
        return True
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")
        return False

def main():
    kontak = {}

    while True:
        tampil_menu()
        pilihan = input("Pilih (1-6): ").strip()

        if pilihan == "1":
            tampil_semua(kontak)

        elif pilihan == "2":
            keyword = input("Masukkan nama / email / telepon: ").strip()
            cari_kontak(kontak, keyword)

        elif pilihan == "3":
            print("=== Tambah kontak baru ===")
            nama = input_nama()

            while True:
                telepon = input("Telepon: ").strip()
                if validasi_telepon(telepon):
                    break

            while True:
                email = input("Email: ").strip()
                if validasi_email(email):
                    break
                else:
                    print("Format email tidak valid.")

            tambah_kontak(kontak, nama, telepon, email)

        elif pilihan == "4":
            nama = input("Nama kontak yang ingin diperbarui: ").strip()
            email_baru = input("Email baru: ").strip()
            update_email(kontak, nama, email_baru)

        elif pilihan == "5":
            nama = input("Nama kontak yang ingin dihapus: ").strip()
            hapus_kontak(kontak, nama)

        elif pilihan == "6":
            print("Keluar. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
