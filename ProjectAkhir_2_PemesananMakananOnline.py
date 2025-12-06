from datetime import datetime

# Data menu makanan
WARUNG_NAME = "WARUNG MAKAN APA AJA"

menu_makanan = [
    {"nama": "Nasi Goreng", "harga": 15000},
    {"nama": "Mie Ayam", "harga": 12000},
    {"nama": "Ayam Geprek", "harga": 18000},
    {"nama": "Soto Ayam", "harga": 13000},
    {"nama": "Es Teh Manis", "harga": 3000},
    {"nama": "Es Jeruk", "harga": 5000},
    {"nama": "Jus Alpukat", "harga": 8000},
    {"nama": "Pisang Goreng", "harga": 5000},
    {"nama": "Tahu Isi", "harga": 6000}
]

keranjang = []
data_pelanggan = {"nama": "", "alamat": "", "catatan": ""}

# Daftar rekening bank
rekening_bank = {
    "1": {"nama": "BNI", "nomor": "1955985472", "atas_nama": "Iqbal Hakim Hakamullah"},
    "2": {"nama": "BCA", "nomor": "245644068118", "atas_nama": "Merrina Sagala"},
}

# Header helper
HEADER_WIDTH = 20

def print_header(title: str):
    print("\n" + "=" * HEADER_WIDTH)
    print(title.center(HEADER_WIDTH))
    print("=" * HEADER_WIDTH)

def is_sabtu():
    return datetime.now().weekday() == 5

def hitung_total():
    subtotal = sum(item['subtotal'] for item in keranjang)
    diskon = subtotal * 0.15 if is_sabtu() else 0
    return subtotal, diskon, subtotal - diskon

def tampil_menu():
    print_header(WARUNG_NAME)
    promo_text = "MENU - DISKON 15% (sabtu)" if is_sabtu() else "MENU"
    print(promo_text.center(HEADER_WIDTH))
    for i, item in enumerate(menu_makanan, 1):
        print(f"{i}. {item['nama']:<18} Rp{item['harga']:>6,}")

def pesan():
    while True:
        tampil_menu()
        try:
            pilih = int(input("Pilih menu (0=selesai): "))
            if pilih == 0:
                break
            if not (1 <= pilih <= len(menu_makanan)):
                print("Menu tidak ada")
                continue
            menu = menu_makanan[pilih - 1]
            jumlah = int(input("Jumlah: "))
            if jumlah <= 0:
                print("Jumlah harus > 0")
                continue
            keranjang.append({
                "menu": menu,
                "jumlah": jumlah,
                "subtotal": menu["harga"] * jumlah
            })
            print(f"Ditambahkan: {menu['nama']} x{jumlah}")
        except ValueError:
            print("Input tidak valid")

def lihat_keranjang():
    print_header("KERANJANG")
    if not keranjang:
        print("Keranjang kosong")
        return
    for i, item in enumerate(keranjang, 1):
        print(f"{i}. {item['menu']['nama']:<15} x{item['jumlah']} = Rp{item['subtotal']:,}")
    subtotal, diskon, total = hitung_total()
    print("--------------------")
    print(f"Subtotal: Rp{subtotal:,}")
    if diskon > 0:
        print(f"Diskon: Rp{diskon:,}")
    print(f"Total: Rp{total:,}")

def hapus_item():
    if not keranjang:
        print("Keranjang kosong")
        return
    lihat_keranjang()
    try:
        nomor = int(input("Hapus nomor (0=batal): "))
        if nomor == 0:
            return
        if 1 <= nomor <= len(keranjang):
            item = keranjang.pop(nomor - 1)
            print(f"Dihapus: {item['menu']['nama']}")
        else:
            print("Nomor tidak valid")
    except ValueError:
        print("Input tidak valid")

def pilih_metode_pembayaran():
    print_header("PILIH BANK")
    for key, bank in rekening_bank.items():
        print(f"{key}. {bank['nama']} - {bank['nomor']} - {bank['atas_nama']}")
    while True:
        pilih = input("Pilih bank (1-2): ")
        if pilih in rekening_bank:
            return rekening_bank[pilih]
        print("Pilihan tidak valid")

def checkout():
    if not keranjang:
        print("Keranjang kosong")
        return
    print_header("CHECKOUT")
    data_pelanggan["nama"] = input("Nama: ")
    data_pelanggan["alamat"] = input("Alamat: ")
    data_pelanggan["catatan"] = input("Catatan (boleh kosong): ")
    bank_dipilih = pilih_metode_pembayaran()
    subtotal, diskon, total = hitung_total()
    waktu_sekarang = datetime.now()
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    nama_hari = hari[waktu_sekarang.weekday()]
    tanggal_waktu = waktu_sekarang.strftime("%d-%m-%Y %H:%M:%S")
    
    print_header("STRUK")
    print(f"{nama_hari}, {tanggal_waktu}")
    print("--------------------")
    print(f"Nama: {data_pelanggan['nama']}")
    print(f"Alamat: {data_pelanggan['alamat']}")
    if data_pelanggan['catatan']:
        print(f"Catatan: {data_pelanggan['catatan']}")
    print("--------------------")
    for i, item in enumerate(keranjang, 1):
        print(f"{i}. {item['menu']['nama']:<15} x{item['jumlah']} = Rp{item['subtotal']:,}")
    print("--------------------")
    print(f"Subtotal: Rp{subtotal:,}")
    if diskon > 0:
        print(f"Diskon: Rp{diskon:,}")
    print(f"Bayar: Rp{total:,}")
    print("====================")
    print("TRANSFER")
    print(f"{bank_dipilih['nama']} {bank_dipilih['nomor']}")
    print(f"Atas Nama: {bank_dipilih['atas_nama']}")
    print(f"Nominal: Rp{total:,}")
    print("====================")
    print("Terimakasih sudah menyelesaikan pesanan.")
    print("Tunggu pesanan Anda sampai di rumah")
    print("====================")
    keranjang.clear()
    
    while True:
        lanjut = input("\nAda pemesan selanjutnya? (y/n): ").lower()
        if lanjut == 'y':
            return
        elif lanjut == 'n':
            print("\nMakasih Bangetttt :)")
            exit()
        else:
            print("Pilihan tidak valid. Ketik 'y' atau 'n'")

def main():
    while True:
        print_header(WARUNG_NAME)
        print("1. Lihat Menu")
        print("2. Pesan")
        print("3. Keranjang")
        print("4. Hapus Item")
        print("5. Checkout")
        print("6. Keluar")
        pilih = input("Pilih: ")
        if pilih == "1":
            tampil_menu()
        elif pilih == "2":
            pesan()
        elif pilih == "3":
            lihat_keranjang()
        elif pilih == "4":
            hapus_item()
        elif pilih == "5":
            checkout()
        elif pilih == "6":
            print("Terima kasih")
            break
        else:
            print("Pilihan tidak valid")
        input("Tekan Enter...")

if __name__ == "__main__":
    main()