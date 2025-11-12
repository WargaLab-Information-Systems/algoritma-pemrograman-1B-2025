kalam = input("Masukkan kata kata hari ini: ").lower()
vokal = "aiueo"
jumlah_vokal = 0
jumlah_kons = 0
jumlah_kata = 1  

for i in kalam:
    if i in vokal:
        jumlah_vokal += 1
    elif i >= "a" and i <= "z":
        jumlah_kons += 1
    elif i == " ":
        jumlah_kata +=1
            
            
print(f"Jumlah huruf vokal    : {jumlah_vokal}")
print(f"Jumlah huruf konsonan : {jumlah_kons}")
print(f"Jumlah kata           : {jumlah_kata}")