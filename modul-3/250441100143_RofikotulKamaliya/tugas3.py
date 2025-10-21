kalimat = input("Masukkan sebuah kalimat: ")
vokal = 'aiueo'
vokal_count = 0
konsonan_count = 0
for char in kalimat:
    if char in vokal:
        vokal_count += 1
    else:
        konsonan_count += 1
kata = kalimat.split()
jumlah_kata = len(kata)
print(f"a. Jumlah huruf vokal: {vokal_count}")
print(f"   Jumlah huruf konsonan: {konsonan_count}")
print(f"b. Jumlah kata dalam kalimat: {jumlah_kata}")