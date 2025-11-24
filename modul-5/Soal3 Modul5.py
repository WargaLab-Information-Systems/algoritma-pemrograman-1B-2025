# Program hitung gaji bersih dengan fungsi
def hitung_gaji_bersih(nama: str, jabatan: str, gaji_pokok: float) -> dict:
    """
    Menghitung komponen gaji:
    - pajak = 5% dari gaji pokok
    - tunjangan = 10% jika Manager, 5% jika Staff, 0% selain itu
    Mengembalikan dict berisi semua nilai untuk ditampilkan.
    """
    pajak_rate = 0.05
    jab_lower = jabatan.strip().lower()

    if jab_lower == "manager":
        tunjangan_rate = 0.10
    elif jab_lower == "staff":
        tunjangan_rate = 0.05
    else:
        tunjangan_rate = 0.0

    pajak = gaji_pokok * pajak_rate
    tunjangan = gaji_pokok * tunjangan_rate
    gaji_bersih = gaji_pokok - pajak + tunjangan

    return {
        "nama": nama,
        "jabatan": jabatan,
        "gaji_pokok": gaji_pokok,
        "pajak_rate": pajak_rate,
        "pajak": pajak,
        "tunjangan_rate": tunjangan_rate,
        "tunjangan": tunjangan,
        "gaji_bersih": gaji_bersih
    }

def format_currency(x: float) -> str:
    """Format angka menjadi string dengan pemisah ribuan dan dua desimal."""
    return f"Rp {x:,.2f}"

def main():
    nama = input("Masukkan nama karyawan: ").strip()
    jabatan = input("Masukkan jabatan (Manager/Staff): ").strip()
    try:
        gaji_input = input("Masukkan gaji pokok (angka, tanpa tanda): ").strip().replace(',', '')
        gaji_pokok = float(gaji_input)
        if gaji_pokok < 0:
            print("Error: gaji pokok harus bernilai positif.")
            return
    except ValueError:
        print("Error: masukkan nilai gaji yang valid (angka).")
        return

    hasil = hitung_gaji_bersih(nama, jabatan, gaji_pokok)

    print("\n--- RINCIAN PERHITUNGAN GAJI ---")
    print(f"Nama            : {hasil['nama']}")
    print(f"Jabatan         : {hasil['jabatan']}")
    print(f"Gaji pokok      : {format_currency(hasil['gaji_pokok'])}")
    print(f"Pajak ({int(hasil['pajak_rate']*100)}%)    : {format_currency(hasil['pajak'])}")
    print(f"Tunjangan ({int(hasil['tunjangan_rate']*100)}%) : {format_currency(hasil['tunjangan'])}")
    print(f"--------------------------------")
    print(f"Gaji bersih     : {format_currency(hasil['gaji_bersih'])}")

if __name__ == "__main__":
    main()