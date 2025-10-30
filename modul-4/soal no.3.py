# Program: Dua Piramida Angka Cermin
  
n = int(input("Masukkan angka n: "))

# Perulangan untuk setiap baris
for i in range(1, n + 1):

    # --- Bagian kiri (angka naik) ---
    for j in range(1, i + 1):
        print(j, end="")  # mencetak angka dari 1 sampai i

    # --- Bagian tengah (spasi) ---
    for k in range(2 * (n - i)):
        print(" ", end="")  # mencetak spasi, jumlahnya berkurang tiap baris

    # --- Bagian kanan (angka turun) ---
    for l in range(i, 0, -1):
        print(l, end="")  # mencetak angka dari i turun ke 1

    print()  # ganti baris setelah satu baris selesai
