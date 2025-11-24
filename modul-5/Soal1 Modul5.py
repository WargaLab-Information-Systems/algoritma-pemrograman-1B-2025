# Program faktorial rekursif (dinamis)
def faktorial(n: int) -> int:
    """Hitung faktorial n secara rekursif. Asumsi: n >= 0."""
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

def main():
    try:
        nilai = int(input("Masukkan bilangan bulat non-negatif N: ").strip())
        if nilai < 0:
            print("Error: Masukkan harus bilangan bulat NON-NEGATIF.")
            return
    except ValueError:
        print("Error: Input harus berupa bilangan bulat.")
        return

    hasil = faktorial(nilai)
    print(f"{nilai}! = {hasil}")

if __name__ == "__main__":
    main()