# Fungsi rekursif untuk menghitung faktorial
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

while True:
    try:
        N = int(input("Masukkan bilangan bulat non-negatif: "))
        if N < 0:
            print("Input tidak boleh negatif! Silakan coba lagi.")
        else:
            break
    except ValueError:
        print("Input harus berupa angka! Silakan coba lagi.")

hasil = faktorial(N)
print(f"Faktorial dari {N} adalah {hasil}")