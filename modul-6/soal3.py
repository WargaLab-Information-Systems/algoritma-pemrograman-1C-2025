# Program CRUD dan Pengecekan Partisi (Versi Ultra-Sederhana)
angka = []

while True:
    print("\nMenu: 1.Tambah 2.Tampilkan 3.Ubah 4.Hapus 5.Cek Partisi 6.Keluar")
    pilihan = input("Pilih: ")
    if pilihan == "1":
        angka.append(int(input("Angka: ")))
        print("Ditambahkan.")
    elif pilihan == "2":
        print("Daftar:", angka or "Kosong.")
    elif pilihan == "3": #mengecek apakah list angka tidak kosong
        if angka:
            #menampilkan daftar agar indeks diketahui 
            print("Daftar:", angka) 
            idx = int(input("Indeks: "))
            if 0 <= idx < len(angka):
                #meminta memasukan indeks yang ingin diubah
                angka[idx] = int(input("Angka baru: "))
                print("Diubah.")
            else:
                print("Indeks invalid.")
        else:
            print("Kosong.")
    elif pilihan == "4":
        if angka:
            print("Daftar:", angka)
            idx = int(input("Indeks: "))
            if 0 <= idx < len(angka):
                removed = angka.pop(idx)
                print(f"{removed} dihapus.")#mencetak teks dengan variabel
            else:
                print("Indeks invalid.") 
        else:
            print("Kosong.")
    elif pilihan == "5":
        if not angka:
            print("Kosong.")
        else:
            total = sum(angka)
            if total % 2:
                print("False: Ganjil.")
            else:
                target = total // 2
                def ss(n, s): return s == target if n < 0 else ss(n-1, s) or (s + angka[n] <= target and ss(n-1, s + angka[n]))
                print("True" if ss(len(angka)-1, 0) else "False")
    elif pilihan == "6":
        break
    else:
        print("Invalid.")