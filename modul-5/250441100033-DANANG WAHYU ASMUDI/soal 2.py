def cek_anagram(kata1, kata2):
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"

    def ubah_ke_kecil(kata):
        hasil = ""
        for huruf in kata:
            ketemu = False
            for i in range(26):
                if huruf == huruf_besar[i]:
                    hasil += huruf_kecil[i]
                    ketemu = True
                    break
            if not ketemu:
                hasil += huruf
        return hasil

    kata1_baru = ubah_ke_kecil(kata1)
    kata2_baru = ubah_ke_kecil(kata2)

    return sorted(kata1_baru) == sorted(kata2_baru)

# Input dari pengguna
kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

# Cek apakah anagram
hasil = cek_anagram(kata_pertama, kata_kedua)

# Tampilkan hasil
if hasil:
    print("Kedua kata tersebut merupakan anagram.")
else:
    print("Kedua kata tersebut bukan anagram.")
