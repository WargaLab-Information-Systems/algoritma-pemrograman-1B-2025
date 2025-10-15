kalimat = input("Masukkan sebuah kalimat: ")

vokal = "aiueo"
jumlah_vokal = 0
jumlah_konsonan = 0

for huruf in kalimat:
        if huruf in vokal:
            jumlah_vokal += 1
        elif huruf.isalpha():
            jumlah_konsonan += 1
else:
    jumlah_kata = len(kalimat.split(""))

print(f"Jumlah huruf vokal     : {jumlah_vokal}")
# print("jumlah huruf vokal:",jumlah_vokal,"vinan")
print(f"Jumlah huruf konsonan  : {jumlah_konsonan}")
print(f"Jumlah kata dalam kalimat : {jumlah_kata}")
# print(f"jumlah kata dalam kalimat : ")