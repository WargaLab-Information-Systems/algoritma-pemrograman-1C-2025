#Soal 1
# Program menentukan nilai huruf dan status kelulusan mahasiswa

# Input
nilai = int(input("Masukkan nilai ujian (0-100): "))
kehadiran = int(input("Masukkan persentase kehadiran (0-100): "))

# Menentukan nilai huruf dan status
if nilai > 85:
    huruf = "A"
    if kehadiran >= 90:
        status = "Lulus dengan Pujian"
    else:
        status = "Lulus"
elif nilai >= 70:
    huruf = "B"
    status = "Lulus"
elif nilai >= 60:
    huruf = "C"
    status = "Lulus"
elif nilai >= 50:
    huruf = "D"
    status = "Tidak Lulus"
else:
    huruf = "E"
    status = "Tidak Lulus"

# Output
print("HASIL PENILAIAN :")
print(f"Nilai huruf: {huruf}")
print(f"Status: {status}")