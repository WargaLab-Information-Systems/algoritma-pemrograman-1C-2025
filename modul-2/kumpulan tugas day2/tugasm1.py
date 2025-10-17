# # Program Menentukan Nilai Huruf dan Status Kelulusan

# # Meminta input dari pengguna
# n_ujian = int(input("Masukkan nilai ujian (0-100): "))
# kehadiran = int(input("Masukkan persentase kehadiran (0-100): "))

# # Menentukan nilai huruf berdasarkan rentang nilai
# if n_ujian > 85:
#     n_huruf = "A"
# elif n_ujian >= 70:
#     n_huruf = "B"
# elif n_ujian >= 60:
#     n_huruf = "C"
# elif n_ujian >= 50:
#     n_huruf = "D"
# else:
#     n_huruf = "E"

# # Menentukan status kelulusan
# if n_ujian >= 85 and kehadiran >= 90:
#     status = "Lulus dengan Pujian"
# elif n_ujian >= 50:
#     status = "Lulus"
# else:
#     status = "Tidak Lulus"

# # Menampilkan hasil akhir
# print("\n=== HASIL PENILAIAN ===")
# print(f"Nilai Ujian      : {n_ujian}")
# print(f"Kehadiran        : {kehadiran}%")
# print(f"Nilai Huruf      : {n_huruf}")
# print(f"Status Kelulusan : {status}")

print("masukkan nilai")
nilai = int(input())
if nilai >= 85:
    print("anda lulus dengan nilai A")
    print("masukkan kehadiran 1-100")
    k = int(input())
    if k >= 90:
        print("lulus dengan pujian")
else:
    if nilai > 85:
        pass
    else:
        if nilai >= 70 and nilai < 85:
            print("anda lulus dengan nilai B")
        else:
            if nilai >= 60 and nilai < 70:
                print("anda lulus dengan nilai C")
            else:
                if nilai >= 50 and nilai < 60:
                    print("coba lagi, karena nilai anda D")
                else:
                    if nilai < 59:
                        print("coba lagi, karena nilai anda E")
                    else:
                        print("hah")
