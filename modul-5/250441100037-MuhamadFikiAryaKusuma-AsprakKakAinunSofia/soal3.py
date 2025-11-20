def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    # Menghitung pajak
    pajak = 0.05 * gaji_pokok

    # Menghitung tunjangan
    if jabatan == "Manager":
        tunjangan = 0.1 * gaji_pokok
    elif jabatan == "Staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    # Menghitung gaji bersih
    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("=== Hasil Perhitungan Gaji ===")
    print("Nama Karyawan:", nama)
    print("Jabatan:", jabatan)
    print("Gaji Pokok:", gaji_pokok)
    print("Pajak (5%):", pajak)
    print("Tunjangan:", tunjangan)
    print("Gaji Bersih:", gaji_bersih)

    return gaji_bersih

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan karyawan: ")
gaji_pokok = float(input("Masukkan gaji pokok karyawan: "))

hitung_gaji_bersih(nama, jabatan, gaji_pokok)