# Program menghitung jumlah huruf vokal, konsonan, dan jumlah kata

kalimat = input("Masukkan sebuah kalimat: ")

vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0

# menghitung huruf vokal dan konsonan
for huruf in kalimat: # hanya hitung huruf (abaikan spasi dan tanda baca).
    if huruf in vokal:
            jumlah_vokal += 1
    else:
            jumlah_konsonan += 1

# menghitung jumlah kata
jumlah_kata = len(kalimat.split()) #split digunakan untuk pemisah kalimat  , len digunakan untuk pengkonversian

print(f"Jumlah huruf vokal   : {jumlah_vokal}")
print(f"Jumlah huruf konsonan: {jumlah_konsonan}")
print(f"Jumlah kata          : {jumlah_kata}")