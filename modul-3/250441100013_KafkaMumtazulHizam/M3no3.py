kalimat = input("Masukkan kalimat: ")

vokal = 0
konsonan = 0
kata = 0
hv = "aiueoAIUEO"
spasi = True

for h in kalimat:
    if h.isalpha():
        if h in hv:
            vokal += 1
        else:
            konsonan += 1

    if h != " " and spasi:
        kata += 1
        spasi = False
    elif h == " ":
        spasi = True

print(f"Jumlah huruf vokal : {vokal}")
print("Jumlah huruf konsonan : {konsonan}")
print("Jumlah kata : {kata}")
