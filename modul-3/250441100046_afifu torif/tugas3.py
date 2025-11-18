kalimat = input("Masukkan kalimat: ").lower()
vokal = "aiueo"
jumlah_vokal = 0
jumlah_konsonan = 0

for huruf in kalimat:
    if huruf.isalpha():   # hanya huruf
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

kata = kalimat.split()
jumlah_kata = len(kata)

print("Jumlah huruf vokal :", jumlah_vokal)
print("Jumlah huruf konsonan :", jumlah_konsonan)
print("Jumlah kata dalam kalimat :", jumlah_kata)