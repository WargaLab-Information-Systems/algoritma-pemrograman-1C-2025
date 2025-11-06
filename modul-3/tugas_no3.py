kalimat = input("Masukkan kalimat:")

huruf_vokal = "aiueoAIUEO"
huruf_konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vokal = 0
konsonan = 0
kata = 0
spasi = True

for huruf in kalimat:
    if huruf.isalpha():
        if huruf in huruf_vokal:
            vokal += 1
        elif huruf in huruf_konsonan:
            konsonan += 1
        spasi = False
    elif huruf == " " and not spasi:
        kata += 1
        spasi = True
        
if not spasi:
    kata += 1

print("Jumlah huruf vokal:", vokal)
print("Jumlah huruf konsonan:", konsonan)
print("Jumlah kata dalam kalimat:", kata)
