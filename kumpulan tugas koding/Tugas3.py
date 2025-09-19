# Hasilnya adalah 18.0
# Karena *, /, //, % di dahulukan, lalu baru ke + dan -, jika prioritasnya (*, /, //, %) lebih dari satu urut saja dari kiri ke kanan
# Urutannya:
# 1.	10+5*2-12/6%3		(5*2 = 10)
# 2.	10+10-12/6%3		(12/6 = 2)
# 3.	10+10-2.0%3			(2.0%3 = 2.0 (karena 2.0 dibagi 3 sisa tetap 2.0))
# 4.	10+10-2.0
# 5.	20-2.0 = 18.0
