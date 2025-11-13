def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]


numbers = []

while True:
    print("\nMenu:")
    print("1. Tambah angka")
    print("2. Tampilkan angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek partisi")
    print("6. Keluar")

    menu = input("Pilih opsi (1-6): ")

    
    if menu == '1':
        try:
            numbers.append(int(input("Masukkan angka: ")))
            print("Angka ditambahkan.")
        except ValueError:
            print("Masukkan angka valid.")

    
    elif menu == '2':
        print("Deretan angka:", numbers if numbers else "Kosong")

    
    elif menu == '3':
        if not numbers:
            print("List masih kosong!")
            continue

        try:
            idx = int(input(f"Masukkan indeks (0-{len(numbers)-1}): "))
            new_val = int(input("Masukkan nilai baru: "))
            if 0 <= idx < len(numbers):
                numbers[idx] = new_val
                print("Angka berhasil diubah.")
            else:
                print("Indeks tidak valid.")
        except ValueError:
            print("Input harus angka.")

    
    elif menu == '4':
        if not numbers:
            print("List masih kosong!")
            continue

        try:
            idx = int(input(f"Masukkan indeks (0-{len(numbers)-1}): "))
            if 0 <= idx < len(numbers):
                print(f"Angka {numbers.pop(idx)} dihapus.")
            else:
                print("Indeks tidak valid.")
        except ValueError:
            print("Input harus angka.")

    elif menu == '5':
        if not numbers:
            print("List masih kosong!")
        else:
            print("Hasil:", can_partition(numbers))

    elif menu == '6':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
