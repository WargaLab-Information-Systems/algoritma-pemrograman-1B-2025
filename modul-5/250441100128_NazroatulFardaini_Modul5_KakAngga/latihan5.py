def hitung_harga_motor(nama, bulan, harga):
    pajak = 0.10 * harga
    if bulan == "september":
        diskon = 0.5 * harga
    elif bulan == "oktober":
        diskon = 0.10 * harga
    else:
        diskon = 0
    total_harga_motor = harga - diskon + pajak
    return total_harga_motor
nama = input("masukkan nama motor: ")
bulan = input("masukkan bulan: ")
harga = int(input("masukkan harga motor: "))

hasil = hitung_harga_motor(nama, bulan, harga)
print(f"total harga motor{nama}yang membeli pada bulan{bulan} adalah Rp {hasil}")



    
