# Mas rusdi kini mengawasi beberapa baris lampu di taman kota, dan setiap baris
# memiliki jumlah lampu yang berbeda. Untuk membantu temannya, mas narji ingin
# membuat program Python yang dapat menampilkan kondisi setiap lampu. Program
# harus meminta input jumlah baris lampu, lalu jumlah lampu di setiap baris. Setiap
# lampu diberi nomor urut, dan program menampilkan pesan “Lampu ke-[x] pada
# baris [y] menyala.” Jika nomor lampu merupakan kelipatan 3, tampilkan “Lampu
# ke-[x] pada baris [y] rusak.” Selain itu, jika baris lampu adalah baris terakhir,
# tambahkan pesan “Periksa sambungan daya utama.” Program ini membantu mas
# rusdi dan temannya mengetahui kondisi setiap lampu dengan cepat dan efisien
# tanpa harus memeriksa secara manual satu per satu.

lampu_baris = int(input("Masukkan jumlah baris lampu: "))
for baris in range(1, lampu_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: "))
    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
    if baris == lampu_baris:
        print("Periksa sambungan daya utama.")
        
