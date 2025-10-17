print("Masukkan kalimat :")
kalimat = input()
vokal = 0
konsonan = 0
spasi = 0
vokal_list = "aeiouAEIOU"
simbol_list = ",.!?;:-_'\"()[]{}@#$%^&*/\\<>~`+=|"
for huruf in kalimat:
    if huruf in vokal_list:
        vokal = vokal + 1
    elif huruf == ' ':
        spasi = spasi + 1
    elif huruf in simbol_list: 
        a = 0  # gak pakai continue
    else:
        konsonan = konsonan + 1
kata = spasi + 1
print("Jumlah huruf vokal:", vokal)
print("Jumlah huruf konsonan:", konsonan)
print("Jumlah kata:", kata)