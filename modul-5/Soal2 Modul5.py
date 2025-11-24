# Fungsi untuk mengecek apakah dua kata adalah anagram
def cek_anagram(kata1, kata2):
    # Ubah huruf jadi huruf kecil semua agar tidak membedakan besar kecil huruf
    kata1 = kata1.lower()
    kata2 = kata2.lower()
    
    # Urutkan huruf dari masing-masing kata
    kata1_urut = sorted(kata1)
    kata2_urut = sorted(kata2)
    
    # Bandingkan hasil pengurutan
    if kata1_urut == kata2_urut:
        return True
    else:
        return False

# Input dari pengguna
kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

# Panggil fungsi dan tampilkan hasil
if cek_anagram(kata_pertama, kata_kedua):
    print("Kedua kata tersebut merupakan anagram!")
else:
    print("Kedua kata tersebut bukan anagram.")