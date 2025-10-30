main
# Tugas no 4

print("= Struk Pembelian IndoMei =")

ulang = "y"

while ulang == "y":
    nama = input("\nMasukkan nama pembeli: ")

    total = 0

    print("Masukkan daftar barang (ketik 'selesai' jika sudah):")
    while True:
        barang = input("Nama barang: ")
        if barang == "selesai":
            break
        harga = int(input("Harga barang: "))
        total = total + harga
        print("Barang ditambahkan!\n")

    print("\n--- STRUK PEMBELIAN ---")
    print("Nama Pembeli:", nama)
    print("Total Harga : Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.\n")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")

print("=== Selamat Datang di IndoMei ===")

while True:  
    print("\n=== Input Data Pembelian ===")
    nama = input("Masukkan nama pembeli: ")

    total = 0
    data_struk = ""

    while True:
        barang = input("Masukkan nama barang (atau ketik 'selesai' untuk berhenti): ")
        if barang.lower() == "selesai":
            break
        try:
            harga = float(input(f"Masukkan harga {barang}: Rp "))
            total += harga
            data_struk += (f"{barang} - Rp {harga}\n")
        except ValueError:
            print("Harga harus berupa angka! Coba lagi.")

  
    print("\n=== STRUK PEMBELIAN INDO MEI ===")
    print(f"Nama Pembeli : {nama}")
    print("----------------------------------")
    print("Barang - Harga (Rp)")
    print("----------------------------------")
    print(data_struk, end="")
    print("----------------------------------")
    print(f"Total Harga : Rp {total}")
    print("----------------------------------")
    print("Terima kasih telah berbelanja di IndoMei! 😊")

    lanjut = input("\nApakah ada pembeli berikutnya? (y/n): ").lower()
    if lanjut != "y":
        print("\n=== Program Selesai ===")
        break
main
