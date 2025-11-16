print("=== PROGRAM PEMBAGIAN ANGKA DOMINIC SZOBOSZLAI ===")

def hitung_data(lst):
    jumlah = 0
    for _ in lst:
        jumlah = jumlah + 1
    return jumlah

def validasi_angka(teks):
    if teks == "":
        return (False, 0)

    negatif = False
    if teks[0] == "-":
        negatif = True
        teks = teks[1:]

    if teks == "":
        return (False, 0)

    nilai = 0
    for t in teks:
        if t < "0" or t > "9":
            return (False, 0)
        nilai = nilai * 10 + (ord(t) - ord("0"))

    if negatif:
        nilai = -nilai

    return (True, nilai)

def tambah_angka(angka):
    print("\n--- TAMBAH ANGKA ---")
    while True:
        teks = input("Masukkan angka (atau ketik 'selesai'): ")
        if teks == "selesai":
            break

        valid, nilai = validasi_angka(teks)
        if not valid:
            print("Data tidak valid, masukkan angka!")
            continue

        baru = []
        for x in angka:
            baru = baru + [x]
        baru = baru + [nilai]
        angka = baru
        print("Angka berhasil ditambah.")

    return angka

def tampilkan_angka(angka):
    print("\n--- DAFTAR ANGKA ---")
    hitung = hitung_data(angka)

    if hitung == 0:
        print("(Belum ada data)")
        return

    print("Daftar angka:", angka)
    nomor = 1
    for x in angka:
        print(nomor, ":", x)
        nomor = nomor + 1


def ubah_angka(angka):
    print("\n--- UBAH ANGKA ---")
    hitung = hitung_data(angka)

    if hitung == 0:
        print("Belum ada data untuk diubah.")
        return angka

    nomor = input("Masukkan nomor data yang ingin diubah: ")

    valid, posisi = validasi_angka(nomor)
    if not valid:
        print("Input tidak valid!")
        return angka

    posisi = posisi - 1
    if posisi < 0 or posisi >= hitung:
        print("Nomor tidak ditemukan!")
        return angka

    baru = input("Masukkan nilai baru: ")
    valid2, nilai_baru = validasi_angka(baru)
    if not valid2:
        print("Masukkan angka yang benar!")
        return angka

    angka[posisi] = nilai_baru
    print("Data berhasil diubah.")
    return angka

def hapus_angka(angka):
    print("\n--- HAPUS ANGKA ---")
    hitung = hitung_data(angka)

    if hitung == 0:
        print("Belum ada data untuk dihapus.")
        return angka

    nomor = input("Masukkan nomor data yang ingin dihapus: ")
    valid, posisi = validasi_angka(nomor)

    if not valid:
        print("Input tidak valid!")
        return angka

    posisi = posisi - 1

    baru = []
    i = 0
    for x in angka:
        if i != posisi:
            baru = baru + [x]
        i = i + 1

    print("Data berhasil dihapus.")
    return baru

def cek_pembagian(angka):
    print("\n--- CEK PEMBAGIAN DUA BAGIAN ---")

    hitung = 0
    total = 0
    for x in angka:
        hitung = hitung + 1
        total = total + x

    if hitung == 0:
        print("Belum ada data.")
        return

    print("Daftar angka:", angka)

    if total % 2 != 0:
        print("False (total ganjil, tidak bisa dibagi sama)")
        return

    kiri = 0
    i = 0
    ketemu = False
    while i < hitung:
        kiri = kiri + angka[i]
        kanan = total - kiri

        if kiri == kanan:
            kiri_bagian = []
            kanan_bagian = []

            j = 0
            while j <= i:
                kiri_bagian = kiri_bagian + [angka[j]]
                j = j + 1
            while j < hitung:
                kanan_bagian = kanan_bagian + [angka[j]]
                j = j + 1

            print("True (bisa dibagi dua sama besar)")
            print("Bagian kiri :", kiri_bagian)
            print("Bagian kanan:", kanan_bagian)
            ketemu = True
            break

        i = i + 1

    if not ketemu:
        print("False (tidak bisa dibagi dua sama besar)")

angka = []

while True:
    print("\nMENU PEMBAGIAN ANGKA DOMINIC SZOBOSZLAI")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Pembagian Dua Bagian")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        angka = tambah_angka(angka)

    elif menu == "2":
        tampilkan_angka(angka)

    elif menu == "3":
        angka = ubah_angka(angka)

    elif menu == "4":
        angka = hapus_angka(angka)

    elif menu == "5":
        cek_pembagian(angka)

    elif menu == "6":
        print("Program selesai. Terima kasih.")
        break

    else:
        print("Pilihan tidak valid!")
