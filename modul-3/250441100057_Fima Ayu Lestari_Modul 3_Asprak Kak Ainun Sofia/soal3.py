 main

# Tugas no 3

kalimat = input("masukkan kalimat: ")

vokal = "aiueoAIUEO"
huruf_abjad = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0
spasi = True

for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal = jumlah_vokal + 1
    elif huruf in huruf_abjad:
        jumlah_konsonan = jumlah_konsonan + 1

    if huruf != " " and spasi == True:
        jumlah_kata = jumlah_kata + 1
        spasi = False
    elif huruf == " ":
        spasi = True

print("Jumlah huruf vokal :", jumlah_vokal)
print("Jumlah huruf konsonan :", jumlah_konsonan)
print("Jumlah kata :", jumlah_kata)

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
main
