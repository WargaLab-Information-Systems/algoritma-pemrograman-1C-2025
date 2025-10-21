# Program Analisis Kalimat
print("=== Program Analisis Kalimat ===")
kalimat = input("Masukkan sebuah kalimat: ")

vokal = 0
konsonan = 0

huruf_vokal = "aiueoAIUEO"

for huruf in kalimat:
    if huruf.isalpha():  # cek apakah karakter adalah huruf
        if huruf in huruf_vokal:
            vokal += 1
        else:
            konsonan += 1

# Hitung jumlah kata (dipisah berdasarkan spasi)
jumlah_kata = len(kalimat.split())

# Tampilkan hasil analisis
print("\n=== Hasil Analisis ===")
print("Jumlah huruf vokal    : ", vokal)
print(f"Jumlah huruf konsonan : {konsonan}")
print(f"Jumlah kata           : {jumlah_kata}")