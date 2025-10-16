print("Masukkan kalimat dan diakhiri dengan '-':")

kalimat = ""
while True:
    baris = input()
    if baris == "-":
        break
    kalimat = kalimat + baris 

vokal = 0
konsonan = 0
jumlah_kata = 0
dalam_kata = 0  # 0 = tidak dalam kata, 1 = sedang dalam kata
jumlah_angka = 0
jumlah_simbol = 0

for huruf in kalimat:

    if (huruf >= "a" and huruf <= "z") or (huruf >= "A" and huruf <= "Z"):
        if huruf == "a" or huruf == "i" or huruf == "u" or huruf == "e" or huruf == "o" or huruf == "A" or huruf == "I" or huruf == "U" or huruf == "E" or huruf == "O":
            vokal = vokal + 1
        else:
            konsonan = konsonan + 1
        
        if dalam_kata == 0:
            jumlah_kata = jumlah_kata + 1
            dalam_kata = 1
    
    elif huruf == " ":
        dalam_kata = 0

    elif huruf >="0" and huruf <= "9":
        jumlah_angka = jumlah_angka + 1
    
    elif huruf == "." or huruf == "," or huruf == "!" or huruf == "?" or huruf == ";" or huruf == ":":
            jumlah_simbol = jumlah_simbol + 1

else:
    dalam_kata = 0

print("Jumlah huruf vokal:", vokal)
print("Jumlah huruf konsonan:", konsonan)
print("Jumlah kata:", jumlah_kata)
print("Jumlah angka:", jumlah_angka)
print("Jumlah simbol:", jumlah_simbol)