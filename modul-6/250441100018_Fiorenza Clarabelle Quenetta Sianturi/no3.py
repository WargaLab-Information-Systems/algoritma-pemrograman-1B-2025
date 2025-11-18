numbers = []

def is_number(s):
    if s == '':
        return False
    for char in s:
        if char < '0' or char > '9':
            return False
    return True

def tambah_angka():
    angka_str = input("masukkan angka yang ingin ditambahkan: ")
    if not is_number(angka_str):
        print("input harus berupa angka positif")
        return
    angka = int(angka_str)
    if angka <= 0:
        print("input harus berupa angka positif")
        return
    numbers.append(angka)
    print(f"angka {angka} berhasil ditambahkan")

def tampilkan_list():
    if not numbers:
        print("List kosong")
    else:
        print("Daftar angka:", numbers)

def ubah_angka():
    tampilkan_list()
    if not numbers:
        return
    index_input = input("masukkan indeks angka yang ingin diubah (dimulai dari 0): ")
    if not is_number(index_input):
        print("indeks harus berupa angka")
        return
    index = int(index_input)
    if 0 <= index < len(numbers):
        angka_input = input("masukkan angka baru: ")
        if not is_number(angka_input):
            print("angka baru harus berupa angka positif")
            return
        angka_baru = int(angka_input)
        if angka_baru <= 0:
            print("angka baru harus berupa angka positif")
            return
        numbers[index] = angka_baru
        print(f"angka di indeks {index} berhasil diubah menjadi {angka_baru}")
    else:
        print("indeks tidak valid")

def hapus_angka():
    tampilkan_list()
    if not numbers:
        return
    index_input = input("masukkan indeks angka yang ingin dihapus (dimulai dari 0): ")
    if not is_number(index_input):
        print("indeks harus berupa angka")
        return
    index = int(index_input)
    if 0 <= index < len(numbers):
        angka = numbers.pop(index)
        print(f"angka {angka} di indeks {index} berhasil dihapus")
    else:
        print("indeks tidak valid")

def find_subset(nums, target):
    def melihat(start, current_sum, path):
        if current_sum == target:
            return path[:]
        for i in range(start, len(nums)):
            if current_sum + nums[i] <= target:
                path.append(nums[i])
                result = melihat(i + 1, current_sum + nums[i], path)
                if result is not None:
                    return result
                path.pop()
        return None
    return melihat(0, 0, [])

def cek_partition():
    if not numbers:
        print("list kosong, tidak dapat dicek")
        return
    total = sum(numbers)
    if total % 2 != 0:
        print("total penjumlahan ganjil, tidak dapat dibagi rata")
        return
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in numbers:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    if dp[target]:
        subset1 = find_subset(numbers, target)
        if subset1 is not None:
            subset2 = numbers[:] 
            for item in subset1:
                subset2.remove(item)  
            print(f"dapat dibagi menjadi dua bagian {subset1} dan {subset2}")
        else:
            print("dapat dibagi menjadi dua bagian dengan jumlah sama")
    else:
        print("tidak dapat dibagi menjadi dua bagian dengan jumlah sama")

def menu():
    while True:
        print("\n===== Program Pengelolaan Angka =====")
        print("1. Tambah angka")
        print("2. Tampilkan daftar angka")
        print("3. Ubah angka")
        print("4. Hapus angka")
        print("5. Cek apakah dapat dibagi menjadi dua bagian dengan jumlah sama")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == "1":
            tambah_angka()
        elif pilihan == "2":
            tampilkan_list()
        elif pilihan == "3":
            ubah_angka()
        elif pilihan == "4":
            hapus_angka()
        elif pilihan == "5":
            cek_partition()
        elif pilihan == "6":
            break
        else:
            print("pilihan tidak ada silakan pilih lagi")

menu()
