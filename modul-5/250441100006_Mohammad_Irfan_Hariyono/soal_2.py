def check_anagram (kata_1, kata_2):
    bersih1 = kata_1 .lower()
    bersih2 = kata_2 .lower()
    if len (bersih1) != len(bersih2):
        return False
    return sorted(bersih1) == sorted(bersih2)

# cek_lagi = True

# while cek_lagi:
input1 = input("\nMasukkan kata pertama: ")
input2 = input ("Masukkan kata kedua: ")


apakah_anagram = check_anagram(input1, input2)

print("\n Hasil ")
if apakah_anagram:
    print(f"Hasil: '{input1}' dan '{input2}' adalah anagram.")
else:
    print(f"Hasil: '{input1}' dan '{input2}' bukan anagram.")

    # mau_cek = input("\nKamu mau cek anagram lagi ? (ya/tidak)")

    # if mau_cek != "ya":
    #     cek_lagi = False