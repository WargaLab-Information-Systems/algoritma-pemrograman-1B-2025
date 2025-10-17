kalimat = input("Masukkan sebuah kalimat untuk dianalisa: ")

jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0

huruf_vokal = "aiueoAIUEO" 
semua_huruf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
print(f"a. Jumlah huruf vokal    : {jumlah_vokal}")
print(f"   Jumlah huruf konsonan : {jumlah_konsonan}")
print(f"b. Jumlah kata dalam kalimat : {jumlah_kata}")
