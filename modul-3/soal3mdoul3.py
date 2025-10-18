#Soal nomor 3
kalimat = input("masukkan kalimat:")
vokal = 0
konsonan = 0
kata = 0
angka = 0

for huruf in kalimat:
    if huruf == " ":
        kata = kata + 1
    elif huruf in "0123456789" :
        angka = angka + 1
    elif huruf in "aiueoAIUEO" :
            vokal = vokal + 1
    elif huruf != " ":
        konsonan = konsonan + 1

print("jumlah huruf vokal", vokal)
print("jumlah konsonan:", konsonan)
print("jumlah angka :", angka)
print("jumlah kata:", kata)
