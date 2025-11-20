
nama = input("Masukkan nama karyawan: ")
             
jabatan = input("Masukkan jabatan (Manager/Staff): ")

def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("\n=== Rincian Gaji Karyawan ===")
    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji Pokok    : Rp {gaji_pokok:,.2f}")
    print(f"Pajak (5%)    : Rp {pajak:,.2f}")
    print(f"Tunjangan     : Rp {tunjangan:,.2f}")
    print(f"Gaji Bersih   : Rp {gaji_bersih:,.2f}")
   
    return gaji_bersih

while True:
    try:
        gaji_pokok = int(input("Masukkan gaji pokok: "))
        if gaji_pokok < 0:
            print("Gaji pokok invalid! Masukkan gaji pokok yang bernilai positif\n")
        else:
            break
    except ValueError:
        print("Input harus berupa angka, bukan huruf atau kalimat! Silakan coba lagi.\n")

hitung_gaji_bersih(nama, jabatan, gaji_pokok)
    