angka_list = []

def tambah(angka):
    angka_list.append(angka)
    print(f"{angka} ditambahkan")

def lihat():
    print(f"List angka: {angka_list}")

def ubah(index, angka_baru):
    if index < len(angka_list):
        lama = angka_list[index]
        angka_list[index] = angka_baru
        print(f"Angka {lama} di index {index} diubah jadi {angka_baru}")
    else:
        print("Index tidak ada")

def hapus(index):
    if index < len(angka_list):
        hapus = angka_list.pop(index)
        print(f"{hapus} dihapus dari index {index}")
    else:
        print("Index tidak ada")

def cek_bagi_dua():
    total = sum(angka_list)
    
    if total % 2 != 0:
        return False
    
    target = total // 2
    
    bisa = [False] * (target + 1)
    bisa[0] = True
    
    for num in angka_list:
        for j in range(target, num - 1, -1):
            if bisa[j - num]:
                bisa[j] = True
                if j == target:
                    return True
    
    return bisa[target]

# Contoh penggunaan
tambah(3)
tambah(4)
tambah(5)
tambah(5)
tambah(4)
tambah(3)

lihat()

hasil = cek_bagi_dua()
print(f"Bisa dibagi dua dengan jumlah sama: {hasil}")

# Contoh ubah dan hapus
ubah(1, 6)
lihat()

hapus(4)
lihat()

hasil_baru = cek_bagi_dua()
print(f"Bisa dibagi dua dengan jumlah sama: {hasil_baru}")