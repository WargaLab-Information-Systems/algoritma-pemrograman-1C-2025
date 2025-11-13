kalimat = input("Masukkan sebuah kalimat: ")

vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0
sebelumnya_spasi = True  # anggap awal sebagai spasi
simbol = ",.!?;:-_'\"()[]{}@#$%^&*/\\<>~`+=|"
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1
    elif huruf in simbol:
        a = 0
    elif (huruf >= 'a' and huruf <= 'z') or (huruf >= 'A' and huruf <= 'Z'):
        jumlah_konsonan += 1

    # Hitung kata: jika huruf bukan spasi dan sebelumnya spasi
    if huruf != ' ' and sebelumnya_spasi:
        jumlah_kata += 1
        sebelumnya_spasi = False
    elif huruf == ' ':
        sebelumnya_spasi = True

# Tampilkan hasil
print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata:", jumlah_kata)