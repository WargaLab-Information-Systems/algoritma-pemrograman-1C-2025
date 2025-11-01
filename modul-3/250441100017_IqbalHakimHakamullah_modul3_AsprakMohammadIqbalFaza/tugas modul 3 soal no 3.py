while True:
    kalimat = input("Masukkan kalimat: ")
    if kalimat:
        break
    print("KALIMAT TIDAK BOLEH KOSONG")

vokal = 0
konsonan = 0
kata = 1
tanda_baca = 0

for huruf in kalimat:
    if huruf == ' ': 
        kata += 1
    elif huruf in 'aiueoAIUEO':
        vokal += 1
    elif huruf in ',:"?/!@#$%^&*)(+_;][{]}]':
        pass
    else:
        konsonan += 1
print(f"Vokal: {vokal}")
print(f"Konsonan: {konsonan}") 
print(f"Kata: {kata}")