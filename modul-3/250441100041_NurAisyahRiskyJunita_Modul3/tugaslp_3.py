# # Program analisa kalimat

# # Input kalimat dari pengguna
# kalimat = input("Masukkan sebuah kalimat: ")

# # Cek apakah kalimat hanya berisi huruf dan spasi
# valid = True
# for huruf in kalimat:
#     if not (huruf.isalpha() or huruf == " "):
#         valid = False
#         break  # hentikan pengecekan jika ada karakter selain huruf/spasi

# if not valid:
#     print("Error: Kalimat hanya boleh mengandung huruf dan spasi!")
# else:
#     # Daftar huruf vokal 
#     vokal = "aiueoAIUEO"

#     # Variabel penghitung
#     jumlah_vokal = 0
#     jumlah_konsonan = 0
#     jumlah_kata = 1  # mulai dari 1 karena kata dipisahkan oleh spasi

#     # Hitung jumlah huruf vokal dan konsonan
#     for huruf in kalimat:
#         if huruf in vokal:
#             jumlah_vokal = jumlah_vokal + 1
#         elif huruf == " ":
#             jumlah_kata = jumlah_kata + 1
#         elif huruf.isalpha():  # hanya huruf (abaikan tanda baca)
#             jumlah_konsonan = jumlah_konsonan + 1

#     # Tampilkan hasil analisa
#     print("\n=== HASIL ANALISA KALIMAT ===")
#     print("Kalimat:", kalimat)
#     print("Jumlah huruf vokal   :", jumlah_vokal)
#     print("Jumlah huruf konsonan:", jumlah_konsonan)
#     print("Jumlah kata          :", jumlah_kata)



# # Program analisa kalimat

# # Input kalimat dari pengguna
# kalimat = input("Masukkan sebuah kalimat: ")

# # Cek apakah hanya berisi huruf dan spasi
# valid = True
# ada_huruf = False

# for huruf in kalimat:
#     if huruf.isalpha():
#         ada_huruf = True  # menandakan ada huruf
#     elif huruf != " ":
#         valid = False     # ada karakter selain huruf/spasi
#         break

# # Jika mengandung angka/simbol atau tidak ada huruf sama sekali
# if not valid or not ada_huruf:
#     print("Error: Kalimat hanya boleh mengandung huruf dan spasi!")
# else:
#     # Daftar huruf vokal 
#     vokal = "aiueoAIUEO"

#     # Variabel penghitung
#     jumlah_vokal = 0
#     jumlah_konsonan = 0
#     jumlah_kata = 1  # mulai dari 1 karena kata dipisahkan oleh spasi

#     # Hitung jumlah huruf vokal dan konsonan
#     for huruf in kalimat:
#         if huruf in vokal:
#             jumlah_vokal = jumlah_vokal + 1
#         elif huruf == " ":
#             jumlah_kata = jumlah_kata + 1
#         elif huruf.isalpha():
#             jumlah_konsonan = jumlah_konsonan + 1

#     # Tampilkan hasil analisa
#     print("\n=== HASIL ANALISA KALIMAT ===")
#     print("Kalimat:", kalimat)
#     print("Jumlah huruf vokal   :", jumlah_vokal)
#     print("Jumlah huruf konsonan:", jumlah_konsonan)
#     print("Jumlah kata          :", jumlah_kata)

# Program analisa kalimat

# Input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Cek apakah kalimat hanya berisi huruf, angka, dan spasi
valid = True
ada_huruf = False

for huruf in kalimat:
    if huruf.isalpha():
        ada_huruf = True
    elif not (huruf.isdigit() or huruf == " "):
        valid = False
        break  # hentikan pengecekan jika ada simbol atau karakter aneh

# Jika ada karakter tidak valid
if not valid:
    print("Error: Kalimat hanya boleh mengandung huruf, angka, dan spasi!")
# Jika tidak ada huruf sama sekali
elif not ada_huruf:
    print("Error: Kalimat harus mengandung minimal satu huruf!")
else:
    # Daftar huruf vokal 
    vokal = "aiueoAIUEO"

    # Variabel penghitung
    jumlah_vokal = 0
    jumlah_konsonan = 0
    jumlah_kata = 1  # mulai dari 1 karena kata dipisahkan oleh spasi

    # Hitung jumlah huruf vokal dan konsonan
    for huruf in kalimat:
        if huruf in vokal:
            jumlah_vokal += 1
        elif huruf == " ":
            jumlah_kata += 1
        elif huruf.isalpha():  # hanya huruf (abaikan angka)
            jumlah_konsonan += 1

    # Tampilkan hasil analisa
    print("\n=== HASIL ANALISA KALIMAT ===")
    print("Kalimat:", kalimat)
    print("Jumlah huruf vokal   :", jumlah_vokal)
    print("Jumlah huruf konsonan:", jumlah_konsonan)
    print("Jumlah kata          :", jumlah_kata)
