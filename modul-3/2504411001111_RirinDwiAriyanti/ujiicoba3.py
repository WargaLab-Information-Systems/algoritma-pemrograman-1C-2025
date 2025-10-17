kalimat = input("Masukkan sebuah kalimat:").lower()
vokal = "abcde"
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

print(f"Jumlah vokal: {jumlah_vokal}")
print(f"Jumlah konsonan: {jumlah_konsonan}")
print(f"Jumlah kata: {jumlah_kata}")