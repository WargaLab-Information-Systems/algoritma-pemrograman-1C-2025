def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    # Hitung tunjangan berdasarkan jabatan (case-insensitive)
    jabatan_lower = jabatan.lower()
    if jabatan_lower == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan_lower == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0  # Jika jabatan lain, tunjangan 0
        print("Peringatan: Jabatan tidak dikenali. Tunjangan dianggap 0.")
    
    # Hitung pajak (5% dari gaji pokok)
    pajak = 0.05 * gaji_pokok
    
    # Hitung gaji bersih
    gaji_bersih = gaji_pokok + tunjangan - pajak
    
    # Tampilkan hasil perhitungan
    print("Nama Karyawan:", nama)
    print("Jabatan:", jabatan)
    print("Gaji Pokok: Rp" + "{:,.1f}".format(gaji_pokok))
    print("Tunjangan: Rp" + "{:,.1f}".format(tunjangan))
    print("Pajak (PPh 5%): Rp" + "{:,.1f}".format(pajak))
    print("Gaji Bersih: Rp" + "{:,.1f}".format(gaji_bersih))
    
    return gaji_bersih

# Program utama untuk input dinamis dengan validasi
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")

try:
    gaji_pokok = float(input("Masukkan gaji pokok: "))
    # Panggil fungsi
    hitung_gaji_bersih(nama, jabatan, gaji_pokok)
except ValueError:
    print("Error: Gaji pokok harus berupa angka. Silakan coba lagi.")