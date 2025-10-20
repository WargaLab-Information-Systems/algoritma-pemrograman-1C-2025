def hitung_karakter_dan_kata(kalimat):
    vokal = "aiueo"
    jumlah_vokal = 0
    jumlah_konsonan = 0

    kata = kalimat.split()
    jumlah_kata = len(kata)

    for char in kalimat:
        if 'a' <= char() <= 'z':
            if char() in vokal:
                jumlah_vokal += 1
            else:
                jumlah_konsonan += 1
    return jumlah_vokal, jumlah_konsonan, jumlah_kata
kalimat_input = input("masukkan sebuah kalimat: ")
jumlah_vokal_hasil, jumlah_konsonan_hasil, jumlah_kata_hasil = hitung_karakter_dan_kata(kalimat_input)

print(f"jumlah huruf vokal: {jumlah_vokal_hasil}")
print(f"jumlah huruf konsonon: {jumlah_konsonan_hasil}")
print(f"jumlah kata: {jumlah_kata_hasil}")