total_kesalahan = 0
batas_kesalahan = 3
pin_saya = 25080

while total_kesalahan < batas_kesalahan:
    pin_atm = int(input("Silahkan masukkan PIN ATM anda : "))
    if pin_atm == pin_saya:
        print("“PIN benar, akses diterima”")
        break
else:
    total_kesalahan += 1
    percobaan_input = batas_kesalahan - total_kesalahan
    print("Sisa percobaan mu",percobaan_input )
if total_kesalahan == batas_kesalahan:
        print("“Akses ditolak, kartu diblokir”")

kalimat = input("Masukkan sebuah kalimat untuk dianalisa: ")
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0
huruf_vokal = "aiueoAIUEO"
semua_huruf = 0
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
dalam_kata = False
for karakter in kalimat:
    if karakter in semua_huruf:
        if karakter in huruf_vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1
    if karakter in semua_huruf and not dalam_kata:
        jumlah_kata += 1
        dalam_kata = True
    elif karakter not in semua_huruf:
        dalam_kata = False
print("--- Hasil Analisa Kalimat ---")
print(f"a. Jumlah huruf vokal : {jumlah_vokal}")
print(f" Jumlah huruf konsonan : {jumlah_konsonan}")
print(f"b. Jumlah kata dalam kalimat : {jumlah_kata}")