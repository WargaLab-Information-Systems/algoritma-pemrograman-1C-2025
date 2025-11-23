# Program menghitung gaji bersih bulanan karyawan

def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    """Fungsi untuk menghitung gaji bersih setelah pajak dan tunjangan"""
    # Pajak tetap sebesar 5%
    pajak = 0.05 * gaji_pokok

    # Tunjangan berdasarkan jabatan
    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0  # Jika jabatan selain Manager atau Staff

    # Hitung gaji bersih
    gaji_bersih = gaji_pokok - pajak + tunjangan

    # Tampilkan hasil perhitungan secara lengkap
    print("\n=== RINCIAN GAJI KARYAWAN ===")
    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji Pokok    : Rp {gaji_pokok:,.2f}")
    print(f"Tunjangan     : Rp {tunjangan:,.2f}")
    print(f"Pajak (5%)    : Rp {pajak:,.2f}")
    print(f"Gaji Bersih   : Rp {gaji_bersih:,.2f}")
    print("===============================")

# Program utama (dinamis)
print("=== Program Hitung Gaji Bersih Karyawan ===")
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (manager/staff): ")

while True:
    try:
        gaji_pokok = float(input("Masukkan gaji pokok: "))
        if gaji_pokok < 0:
            print("Gaji pokok tidak boleh negatif! Silakan coba lagi.")
        else:
            break
    except ValueError:
        print("Input harus berupa angka! Silakan coba lagi.")


hitung_gaji_bersih(nama, jabatan, gaji_pokok)