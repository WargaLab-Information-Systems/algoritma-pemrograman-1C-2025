# #MENGHITUNG GAJI KARYAAWAN SECARA DINAMIS DENGAN MENGIMPUT NAMA, JABATAN DAN GAJI POKOK

def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak_penghasilan = 0.05 * gaji_pokok

    if jabatan == "manager": 
        tunjangan = 0.10 * gaji_pokok
    elif jabatan== "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak_penghasilan + tunjangan
    print("\n=== HASIL PERHITUNGAN ===")
    print(f"Nama karyawan : {nama}")
    print(f"Jabatan : {jabatan}")
    print(f"Gaji pokok : {gaji_pokok}")
    print(f"Pajak (5%) : {pajak_penghasilan}")
    print(f"Tunjangan : {tunjangan}")
    print(f"Gaji bersih : {gaji_bersih}")


# ==== PROGRAM UTAMA ====
print("\n=== PROGRAM MENGHITUNG GAJI KARYAWAN ===")
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager / Staff / Lainnya): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)



