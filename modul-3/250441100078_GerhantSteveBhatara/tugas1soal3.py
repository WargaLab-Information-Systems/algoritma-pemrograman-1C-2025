kalimat = input("Masukkan kalimat: ").lower()
vokal = "aiueo"
j_vokal = 0
j_konsonan = 0

for huruf in kalimat:
    if huruf.isalpha():
        if huruf in vokal:
            j_vokal += 1
        else:
            j_konsonan += 1
            
j_kata = len(kalimat.split())

print("Jumlah huruf vokal:", j_vokal)
print("Jumlah huruf konsonan:", j_konsonan)
print("Jumlah kata:", j_kata)