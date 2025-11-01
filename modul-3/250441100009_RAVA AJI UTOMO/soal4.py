# Loop utama untuk pelanggan berikutnya
while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    # Variabel untuk total harga dan daftar barang
    total_harga = 0
    daftar_barang = ""
    # Loop untuk input setiap barang
    i = 0
    while i < jumlah_barang:
        nama_barang = input("Masukkan nama barang ke-" + str(i + 1) + ": ")
        harga_barang = int(input("Masukkan harga barang: "))
        daftar_barang = daftar_barang + nama_barang + " - Rp " + str(harga_barang) + "\n"  # penambahan ke teks daftar barang
        total_harga = total_harga + harga_barang # Tambahkan ke total harga
        i = i + 1
    # Tampilan struk
    print("STRUK PEMBELIAN INDOMEI")
    print("Nama Pembeli:", nama_pembeli)
    print("Daftar Barang:")
    print(daftar_barang)
    print("Total Harga: Rp", total_harga)
    print("Terima kasih telah berbelanja di IndoMei.")
    # buat tanya
    jawaban = input("Ada yang beli lagi? (tdk/ya): ")
    if jawaban == "tdk":
        break
