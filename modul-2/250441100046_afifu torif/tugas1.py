base_price = 50000

discount_catalogue = {
    "anak_anak": 50,
    "pelajar": 30,
    "selasa": 20,
}

def hitung_harga_tiket(usia: int, pelajar: str, hari: str) -> int:
    """Menghitung harga tiket berdasarkan usia, status pelajar, dan hari."""
    diskon_kandidat = []

    if usia < 12:
        diskon_kandidat.append(discount_catalogue["anak_anak"])

    if pelajar.strip().lower() == "pelajar":
        diskon_kandidat.append(discount_catalogue["pelajar"])

    if hari.strip().lower() == "selasa":
        diskon_kandidat.append(discount_catalogue["selasa"])

    # Ambil diskon tertinggi
    diskon = max(diskon_kandidat) if diskon_kandidat else 0

    # Hitung harga akhir
    harga_akhir = base_price * (100 - diskon) // 100
    return harga_akhir

# Program utama
print("=== Pemesanan Tiket Bioskop ===")
usia = int(input("Usia penonton: "))
pelajar = input("Apakah pelajar SMA dengan kartu pelajar (ya/tidak)? ")
hari = input("Hari menonton (misalnya: selasa): ")

bayar = hitung_harga_tiket(usia, pelajar, hari)
print(f"Harga tiket yang harus dibayar: Rp {bayar:,}")