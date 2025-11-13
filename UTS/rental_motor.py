# =====================================================
#   PROGRAM RENTAL MOTOR ACONK
#   Versi Lengkap (Memenuhi Semua Kriteria)
# =====================================================

def tampilkan_menu():
    print("\n=== RENTAL MOTOR ACONK ===")
    print("Daftar Harga Sewa per Hari:")
    print("1. Motor Matic  = Rp 50.000")
    print("2. Motor Trail  = Rp 100.000")
    print("3. Motor Sport  = Rp 75.000")
    print("=============================")


def hitung_biaya(jenis, lama_sewa, kupon):
    # Harga motor per hari
    harga_motor = {
        "1": 50000,
        "2": 100000,
        "3": 75000
    }

    # Validasi input motor
    if jenis not in harga_motor:
        print("❌ Jenis motor tidak valid! Silakan pilih 1, 2, atau 3.")
        return None

    # Menentukan nama motor
    nama_motor = {"1": "Matic", "2": "Trail", "3": "Sport"}[jenis]
    harga_per_hari = harga_motor[jenis]

    # Hitung subtotal (tanpa asuransi/diskon)
    subtotal = harga_per_hari * lama_sewa

    # Asuransi berlaku kelipatan Rp15.000 tiap 3 hari (jika > 3 hari)
    asuransi = (lama_sewa // 3) * 15000 if lama_sewa > 3 else 0

    # Total sebelum diskon
    total_sementara = subtotal + asuransi

    # Diskon 10% jika subtotal > Rp150.000 (tidak berlaku kelipatan)
    diskon_subtotal = 0
    if subtotal > 150000:
        diskon_subtotal = total_sementara * 0.10

    # Diskon tambahan 5% jika pakai kupon "AconkGG" (Case Sensitive)
    diskon_kupon = 0
    if kupon == "AconkGG":
        diskon_kupon = (total_sementara - diskon_subtotal) * 0.05

    # Hitung total akhir
    total_bayar = total_sementara - diskon_subtotal - diskon_kupon

    # Cetak struk pembayaran
    print("\n===== STRUK PEMBAYARAN =====")
    print(f"Jenis Motor        : {nama_motor}")
    print(f"Harga per Hari     : Rp {harga_per_hari:,}")
    print(f"Lama Sewa          : {lama_sewa} hari")
    print(f"Subtotal           : Rp {subtotal:,}")
    print(f"Asuransi           : Rp {asuransi:,}")

    # Tampilkan kondisi diskon
    if diskon_subtotal > 0:
        print(f"Diskon Subtotal    : Rp {diskon_subtotal:,.0f}")
    else:
        print("Diskon Subtotal    : Tidak Dapat Diskon")

    if diskon_kupon > 0:
        print(f"Diskon Kupon       : Rp {diskon_kupon:,.0f}")
    else:
        print("Diskon Kupon       : Tidak Ada Kupon / Salah")

    print("--------------------------------")
    print(f"TOTAL BAYAR        : Rp {total_bayar:,.0f}")
    print("================================")
    print("Terima kasih telah menggunakan layanan Rental Motor Aconk!\n")

    return total_bayar


# ============== PROGRAM UTAMA ==============
while True:
    tampilkan_menu()

    # Input nama dan pilihan
    nama = input("Masukkan nama penyewa: ")
    jenis = input("Pilih jenis motor (1/2/3): ")

    # Validasi input hari
    try:
        lama = int(input("Masukkan lama sewa (hari): "))
        if lama <= 0:
            print("❌ Lama sewa harus lebih dari 0 hari!")
            continue
    except ValueError:
        print("❌ Input hari harus berupa angka!")
        continue

    # Input kupon opsional
    kupon = input("Masukkan kode kupon (jika ada): ")

    # Proses perhitungan
    hasil = hitung_biaya(jenis, lama, kupon)
    if hasil is None:
        continue

    # Tanya apakah ingin sewa lagi
    ulang = input("Apakah ingin melakukan penyewaan lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Program selesai. Sampai jumpa!")
        break
