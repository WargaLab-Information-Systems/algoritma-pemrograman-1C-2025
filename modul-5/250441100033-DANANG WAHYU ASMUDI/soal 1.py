def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

while True:
    input_user = input("Masukkan bilangan bulat non-negatif: ")

    # Validasi input
    if "." in input_user or "-" in input_user:
        print("Input tidak valid. Harap masukkan bilangan bulat non-negatif.")
        continue

    if not input_user.isdigit():
        print("Input harus berupa angka bulat. Silakan coba lagi.")
        continue

    N = int(input_user)
    hasil = faktorial(N)
    print(f"Faktorial dari {N} adalah {hasil}")
    break