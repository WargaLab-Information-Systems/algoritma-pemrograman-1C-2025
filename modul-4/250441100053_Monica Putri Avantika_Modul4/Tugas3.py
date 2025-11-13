# Program membuat dua piramida angka saling berhadapan (cermin)

# Input jumlah baris
n = int(input("Masukkan jumlah baris (n): "))

print(" === Pola Piramida Cermin === ")

# Perulangan untuk setiap baris
for i in range(1, n + 1):

    # --- 1. Piramida kiri (angka naik dari 1 sampai i) ---
    for j in range(1, i + 1):
        print(j, end=" ")

    # --- 2. Spasi tengah (menjaga simetri) ---
    # Jumlah spasi menurun setiap baris
    for d in range(2 * (n - i)):
        print("  ", end="")

    # --- 3. Piramida kanan (angka turun dari i ke 1) ---
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()  # Pindah ke baris berikutnya 


