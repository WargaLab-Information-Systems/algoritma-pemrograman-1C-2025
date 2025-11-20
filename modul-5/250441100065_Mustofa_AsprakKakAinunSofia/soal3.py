# Program Menghitung Gaji Bersih Karyawan
def hitung_gaji(nama, jabatan, gaji_pokok):

    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    pph = 0.05 * gaji_pokok
    gaji_bersih = gaji_pokok - pph + tunjangan

    print("\n=== Rincian Gaji Karyawan ===")
    print(f"Nama Karyawan   : {nama}")
    print(f"Jabatan         : {jabatan}")
    print(f"Gaji Pokok      : Rp {gaji_pokok:,.2f}")
    print(f"Tunjangan       : Rp {tunjangan:,.2f}")
    print(f"Pph (5%)      : Rp {pph:,.2f}")
    print(f"Gaji Bersih     : Rp {gaji_bersih:,.2f}")

nama = input("Masukkan nama karyawan: ")
while True:
    jabatan = input("Masukkan jabatan (Manager/Staff): ")
    if jabatan.lower() not in ("manager", "staff"):
        print("Jabatan tidak valid! Harap masukkan 'Manager' atau 'Staff'.")
    else:
        break

while True:
    try:
        gaji_pokok = float(input("Masukkan gaji pokok: "))
        if gaji_pokok < 0:
            print("Gaji pokok tidak boleh negatif! Silakan coba lagi.")
        else:
            break
    except ValueError:
        print("Input harus berupa angka! Silakan coba lagi.")

hitung_gaji(nama, jabatan, gaji_pokok)