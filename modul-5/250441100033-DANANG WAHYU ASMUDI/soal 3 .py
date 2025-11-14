def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    pajak = gaji_pokok * 5 / 100

    if jabatan == "Manager" or jabatan == "manager" or jabatan == "MANAGER":
        tunjangan = gaji_pokok * 10 / 100
    elif jabatan == "Staff" or jabatan == "staff" or jabatan == "STAFF":
        tunjangan = gaji_pokok * 5 / 100

    # Hitung gaji bersih
    gaji_bersih = gaji_pokok - pajak + tunjangan

    # Tampilkan hasil
    print("\n=== RINCIAN GAJI KARYAWAN ===")
    print("Nama Karyawan  :", nama)
    print("Jabatan        :", jabatan)
    print("Gaji Pokok     : Rp", gaji_pokok)
    print("PPh (5%)       : Rp", pajak)
    print("Tunjangan      : Rp", tunjangan)
    print("Gaji Bersih    : Rp", gaji_bersih)
    print("=============================")

# Input dari pengguna
nama_input = input("Masukkan nama karyawan: ")

# Validasi jabatan
while True:
    jabatan_input = input("Masukkan jabatan (Manager/Staff): ")
    if jabatan_input in ["Manager", "manager", "MANAGER", "Staff", "staff", "STAFF"]:
        break
    else:
        print("Input jabatan tidak valid! Harus 'Manager' atau 'Staff'. Silakan coba lagi.")

gaji_input = int(input("Masukkan gaji pokok: "))

# Panggil fungsi
hitung_gaji_bersih(nama_input, jabatan_input, gaji_input)