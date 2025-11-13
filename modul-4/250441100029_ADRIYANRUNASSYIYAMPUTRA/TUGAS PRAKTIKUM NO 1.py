jumlahbaris=int(input("input jumlah baris yang akan di buat "))
for baris in range  (1,jumlahbaris+1):
    print(f"masukkan jumlah lampu pada baris ke = {baris}")
    jumlahlampu=int(input("input jumlah lampu"))
    for lampu in range (1,jumlahlampu+1):
        if lampu % 3 == 0:
            print(f" lampu pada ke {lampu} di baris ke {baris} rusak")
        else:
            print(f" lampu pada ke {lampu} di baris ke {baris} menyala")

print("periksa sambungan daya utama")