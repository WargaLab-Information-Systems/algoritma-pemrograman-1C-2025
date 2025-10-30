def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    pajak = 00.05 * gaji_pokok
    tunjangan = 0
    if jabatan == "manajer":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok

    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("\n=== hasil perhitungan gaji ===")
    print(f"nama karyawan: {nama}")
    print(f"jabatan: {jabatan}")
    print(f"gaji pokok: Rp {gaji_pokok:,.2f}")
    print(f"pajak PPh (5%): Rp {pajak:,.2f}")
    print(f"tunjangan: Rp {tunjangan:,.2f}")
    print(f"gaji bersih: Rp {gaji_bersih:,.2f}")

    return gaji_bersih

nama_karyawan = input("masukkan nama karyawan: ")
jabatan_karyawan = input("masukkan jabatan (manajer/staff): ")
gaji_pokok_karyawan = float(input("masukkan gaji pokok): "))

hitung_gaji_bersih(nama_karyawan, jabatan_karyawan, gaji_pokok_karyawan)