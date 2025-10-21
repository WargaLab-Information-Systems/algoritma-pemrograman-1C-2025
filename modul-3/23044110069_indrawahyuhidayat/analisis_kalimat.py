# Program analisis kalimat
# Menampilkan jumlah huruf vokal, konsonan, dan kata dalam kalimat

print("=== Program Analisis Kalimat ===")

# Meminta input kalimat dari user
kalimat = input("Masukkan sebuah kalimat: ")

# Mengubah semua huruf menjadi huruf kecil agar lebih mudah dihitung
kalimat_lower = kalimat.lower()

# Daftar huruf vokal
vokal = "aiueo"

# Inisialisasi penghitung
jumlah_vokal = 0
jumlah_konsonan = 0

# Menghitung jumlah vokal dan konsonan
for huruf in kalimat_lower:
    if huruf.isalpha():  # Mengecek apakah karakter adalah huruf
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

# Menghitung jumlah kata dengan memisahkan spasi
jumlah_kata = len(kalimat.split())

# Menampilkan hasil analisis
print("\n=== Hasil Analisis ===")
print(f"Jumlah huruf vokal    : {jumlah_vokal}")
print(f"Jumlah huruf konsonan : {jumlah_konsonan}")
print(f"Jumlah kata           : {jumlah_kata}")
