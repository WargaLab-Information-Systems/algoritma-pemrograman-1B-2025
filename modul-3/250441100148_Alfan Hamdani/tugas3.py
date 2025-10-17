# Program untuk menganalisis kalimat
kalimat = input("Masukkan sebuah kalimat: ")

jumlah_vokal = 0
jumlah_konsonan = 0

vokal = "aiueoAIUEO"

# hitung vokal dan konsonan
for huruf in kalimat: #untuk membaca setiap karakte yang ada di dalam kalimat
    if huruf.isalpha(): #cek apakah huruf (bukan spasi/angka/simbol)
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

# hitung jumlah kata
kata = kalimat.split() #memisahkan kalimat berdasrkan spasi
jumlah_kata = len(kata)

print("Jumlah huruf vokal   :", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata          :", jumlah_kata)