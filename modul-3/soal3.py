
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