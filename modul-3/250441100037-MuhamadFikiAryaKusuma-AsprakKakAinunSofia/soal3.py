kalimat = input("Masukkan sebuah kalimat: ")
vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 1
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1
    elif huruf.isalpha(): # isalpha() untuk mengecek apakah karakter adalah huruf
        jumlah_konsonan += 1
    elif huruf == " ":
        jumlah_kata += 1

print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata:", jumlah_kata)