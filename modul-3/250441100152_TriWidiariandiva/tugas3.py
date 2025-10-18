kalimat = input("Masukkan kalimat: ")

alfabet = "abcdefghijklmnopqrstuvwxyz"
vokal = "aiueo"
konsonan = "bcdfghjklmnpqrstvwxyz"
jumlah_vokal = 0 
jumlah_konsonan = 0 
jumlah_kata = 0 
dalam_kata = False

for huruf in kalimat.lower():
    if huruf in alfabet:
        if huruf in vokal:
            jumlah_vokal += 1 
        else: 
            jumlah_konsonan += 1

    if huruf != " " and not dalam_kata:
        jumlah_kata += 1
        dalam_kata = True
    elif huruf == " ":
        dalam_kata = False

print("Jumlah huruf vokal:", jumlah_vokal) 
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata:", jumlah_kata)