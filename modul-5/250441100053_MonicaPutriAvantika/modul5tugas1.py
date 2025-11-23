# Program menghitung faktorial secara rekursif
# Kasus: Pak Tungtung ingin membuka brankas berisi private key Bitcoin

def faktorial(n):
    """Fungsi rekursif untuk menghitung faktorial dari n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Program utama bersifat dinamis (input dari pengguna)
try:
    n = int(input("Masukkan bilangan bulat non-negatif (N): "))
    if n < 0:
        print("Maaf, bilangan tidak boleh negatif.")
    else:
        hasil = faktorial(n)
        print(f"Hasil faktorial dari {n}! = {hasil}")
except ValueError:
    print("Input tidak valid! Harap masukkan bilangan bulat.")
