def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok
    tunjangan = 0.10 * gaji_pokok if jabatan == "Manager" else 0.05 * gaji_pokok
    gaji_bersih = gaji_pokok + tunjangan - pajak

    print("\n=== Rincian Gaji Karyawan ===")
    print(f"Nama       : {nama}")
    print(f"Jabatan    : {jabatan}")
    print(f"Gaji Pokok : {gaji_pokok}")
    print(f"Tunjangan  : {tunjangan}")
    print(f"Pajak (5%) : {pajak}")
    print(f"Gaji Bersih: {gaji_bersih}")


nama = input("Masukkan nama karyawan: ")
if not nama.isalpha():
    print("Nama hanya boleh huruf!")
    exit()

jabatan = input("Masukkan jabatan (Manager/Staff): ")
if not jabatan.isalpha():
    print("Jabatan hanya boleh huruf!")
    exit()

gaji = float(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji)
