def hitung_faktorial(n):
    # Jika n adalah 0 atau 1, hasilnya selalu 1
    if n == 0 or n == 1:
        return 1
    # Jika n lebih dari 1, hitung n * faktorial(n-1)
    else:
        return n * hitung_faktorial(n - 1)

# Program utama
print("=== PROGRAM FAKTORIAL ===")

# Input dari user
angka = int(input("Masukkan angka: "))

# Hitung dan tampilkan hasil
hasil = hitung_faktorial(angka)
print(f"{angka}! = {hasil}")