kalimat = input("Masukkan sebuah kalimat: ")

vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0

for huruf in kalimat:
    if huruf.isalpha():  # hanya menghitung huruf
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

# digunakan untuk menghitung pamjang atau umtuk menghitung jumlah kata (dipisahkan oleh spasi)
jumlah_kata = len(kalimat.split())

print("\nHasil analisis:")
print("Jumlah huruf vokal    :", jumlah_vokal)
print("Jumlah huruf konsonan :", jumlah_konsonan)
print("Jumlah kata           :", jumlah_kata)