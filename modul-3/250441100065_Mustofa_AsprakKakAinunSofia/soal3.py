# Program Analisa Kalimat
print("=== Program Analisa Kalimat ===")
kalimat = input("Masukkan sebuah kalimat: ")

vokal = 0
konsonan = 0

# Daftar huruf vokal
huruf_vokal = "aiueoAIUEO"

# Hitung vokal dan konsonan
for huruf in kalimat:
    if huruf in huruf_vokal:
        vokal = vokal + 1
    elif huruf != " 0": 
        konsonan = konsonan + 1
 
spasi = 0
for huruf in kalimat:
    if huruf == " ":
        spasi = spasi + 1
jumlah_kata = spasi + 1

print("Jumlah huruf vokal   :", vokal)
print("Jumlah huruf konsonan:", konsonan)
print("Jumlah kata          :", jumlah_kata)

# contoh mengunakan isalpha() dan split()
# # Program Analisa Kalimat
# print("=== Program Analisa Kalimat ===")
# kalimat = input("Masukkan sebuah kalimat: ")

# # Inisialisasi jumlah huruf
# vokal = 0
# konsonan = 0

# # Huruf vokal
# huruf_vokal = "aiueoAIUEO"

# # Hitung huruf vokal dan konsonan
# for huruf in kalimat:
#     if huruf in huruf_vokal:
#         vokal = vokal + 1
#     elif huruf.isalpha():  # cek apakah huruf
#         konsonan = konsonan + 1

# # Hitung jumlah kata
# kata = kalimat.split()
# jumlah_kata = len(kata)

# # Tampilkan hasil
# print("Jumlah huruf vokal   :", vokal)
# print("Jumlah huruf konsonan:", konsonan)
# print("Jumlah kata          :", jumlah_kata)
