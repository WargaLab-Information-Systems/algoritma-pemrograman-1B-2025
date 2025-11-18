kalimat = input("Masukkan kalimat :")
vokal = "aiueoAIUEO"
konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
angka = "0123456789"
jumlah_vokal = 0
jumlah_konsonan = 0 
jumlah_kata = 0 
spasi_sebelumnya = True
ada_angka = False
for huruf in kalimat:
    if huruf in angka:
        ada_angka = True
        break

if ada_angka:
    print("Kalimat tidak bisa mengandung angka")
    
    if huruf in vokal:
        jumlah_vokal = jumlah_vokal + 1 
    if huruf in konsonan : 
        jumlah_konsonan = jumlah_konsonan + 1 
    if huruf == " ":
        spasi_sebelumnya = True
    else :
        if spasi_sebelumnya :
            jumlah_kata = jumlah_kata + 1 
        spasi_sebelumnya = False
print(f" Jumlah huruf vokal : {jumlah_vokal}")
print(f" Jumlah huruf konsonan : {jumlah_konsonan}")
print(f" Jumlah kata : {jumlah_kata}")