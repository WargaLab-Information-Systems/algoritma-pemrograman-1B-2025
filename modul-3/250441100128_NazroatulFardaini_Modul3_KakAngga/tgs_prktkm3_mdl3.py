# input untuk memasukkan kalimat
kalimat = input("masukkan sebuah kalimat: ")
# variabel jumlah vokal, jumlah kata, dan jumlah konsonan
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0
# huruf vokal dan alfabet
vokal = "aiueo"
alfabet = "abcdefghijklmnopqrstuvwxyz"
# menghitung huruf vokal dan konsonan
for huruf in kalimat:
    if huruf in alfabet:
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1
    
# menghitung jumlah kata
dalam_kata = False # apakah sedang berada didalam kata
for huruf in kalimat:
    if huruf != " ":
        if dalam_kata == False:
            jumlah_kata += 1
            dalam_kata = True
    else:
        dalam_kata = False
# menampilkan hasil
print("jumlah huruf vokal :", jumlah_vokal)
print("jumlah huruf konsonan :", jumlah_konsonan)
print("jumlah kata dalam kalimat :", jumlah_kata)