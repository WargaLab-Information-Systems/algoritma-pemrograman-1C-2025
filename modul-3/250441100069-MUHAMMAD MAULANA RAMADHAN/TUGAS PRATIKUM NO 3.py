kalimat = input("Masukkan sebuah kalimat: ")

vokal = 0
konsonan = 0
kata = 1
i = 0

while i < len(kalimat):
    char = kalimat[i]
    if 'a' <= char.lower() <= 'z':
        if char.lower() == 'a' or char.lower() == 'i' or char.lower() == 'u' or char.lower() == 'e' or char.lower() == 'o':
            vokal = vokal + 1
        else:
            konsonan = konsonan + 1
    if char == ' ':
        kata = kata + 1
    i = i + 1

print("\nAnalisa Kalimat:")
print("a. Jumlah huruf vokal:", vokal)
print("b. Jumlah huruf konsonan:", konsonan)
print("c. Jumlah kata dalam kalimat:", kata)
