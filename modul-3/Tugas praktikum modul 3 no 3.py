kalimat = input("masukkan sebuah kalimat:")

vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0

for huruf in kalimat:
    if huruf.isalpha():
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

kata = kalimat.split()
jumlah_kata = len(kata)

print("jumlah huruf vokal:", jumlah_vokal)
print("jumlah huruf konsonan:", jumlah_konsonan)
print("jumlah kata:", jumlah_kata)

