kontak = {

}
list_nomer_telepon=[]
list_email=[]

def menambah_kontak():
    while True: #wadah looping inputan nama kontak baru
        print("input nama , N untuk selesai")#penyelesaian
        nama=str(input("input nama = ")) # user input nama untuk key baru
        if nama in ["N","n"]:
             break
        elif nama in kontak: #pengecekan nama kontak supaya terhindar dari nama kontak ganda
            print("kontak sudah ada , silahkan input nama kontak yang berbeda")
        else: #lanjut program selanjutnya
            kontak[nama] = {} # untuk proses pembuatan key baru dari value nama namun untuk value nya masih kosong 
            while True:#perulangan untuk menangani nomer telepon yang ganda
                nomer_telepon=str(input("input nomer telepon = ")) # user meng input nomer telepon
                if nomer_telepon in list_nomer_telepon: #pengecekan inputan user ke data base nomer telepon
                    print("ada nomer telepon ganda dan gunakan nomer telepon lain") #user akan di suruh untuk menggunakan nomer telepon lain jika ada yang sama
                elif nomer_telepon not in list_nomer_telepon:#nomer telepon tidak ganda
                    list_nomer_telepon.append(nomer_telepon) #nomer telepon terbaru di uploud le data base nomer telepon
                    break # perulangan inputan nomer telepon sudah selesai
            kontak[nama]['no_telp'] = [nomer_telepon] #akan mengisi dan membuat key baru bernama no telepon dan value nomer telepon nya
            while True: 
                email=str(input("input nama depan tanpa @gmail.com =  ")) # user meng input nama depan tidak pakai @gmail.com, pengecekan jika ganda nanti akan mengulang
                if email in list_email:#di sini letak pengecekan nya 
                    print("ada email ganda,gunakan email lain")
                elif email not in list_email: #jika email nya masih baru
                    kontak[nama]['email']=[email+"@gmail.com"]# membuat key email beserta value nya 
                    list_email.append(email+"@gmail.com")#nama depan email di tambahkan ke data base list_email
                    break #looping berhenti           


def perbarui_no_telepon():
        while True:
            memilih_key=str(input("input nama kontak yang ingin di perbarui no telepon nya = "))# kurang untuk pemberhentian 
            if kontak.get(memilih_key) is not None:
                print(f" kontak '{memilih_key}' ") #lanjutkan nanti 
                perbarui_nomor=str(input("input nomer baru"))
                sebelum=kontak[memilih_key]['no_telp']
                di_stringkan=''.join(sebelum)
                list_nomer_telepon.remove(di_stringkan)
                kontak[memilih_key]['no_telp']=[perbarui_nomor]
                list_nomer_telepon.append(perbarui_nomor)
                break
            else:
                print(" kontak tidak di temukan , input dengan benar")#jangan lupa di buat while

def perbarui_email():
        while True:
            memilih_key=str(input("input nama kontak yang ingin di perbarui emaail nya = "))# kurang untuk pemberhentian 
            if kontak.get(memilih_key) is not None:
                print(f" kontak '{memilih_key}' ") #lanjutkan nanti 
                perbarui_email=str(input("input email baru"))
                sebelum=kontak[memilih_key]['email']
                di_stringkan=''.join(sebelum)
                print(di_stringkan)
                list_email.remove(di_stringkan)
                kontak[memilih_key]['email']=[perbarui_email+"@gmail.com"]
                list_email.append(perbarui_email+"@gmail.com")
                break
            else:
                print(" kontak tidak di temukan , input dengan benar")#jangan lupa di buat while  

def menghapus():
    while True:
            memilih_key=str(input("input nama kontak yang ingin di hapus"))# kurang untuk pemberhentian 
            if kontak.get(memilih_key) is not None:
                print(f" Key '{memilih_key}' ada dan di hapus") #lanjutkan nanti
                email_sebelum=kontak[memilih_key]['email']
                di_stringkan_e=''.join(email_sebelum)
                list_email.remove(di_stringkan_e)
                nomer_sebelum=kontak[memilih_key]['no_telp']
                di_stringkan_p=''.join(nomer_sebelum)
                list_nomer_telepon.remove(di_stringkan_p)
                del kontak[memilih_key]
                break
            else:
                print(" Key '' tidak ada")#jangan lupa di buat while
              

def output_data():
    print("==============================DAFTAR KONTAK ==============================")
    print()
    for nama in kontak: #untuk output 
        print("nama       = ",nama)
        print("no telepon = ",kontak[nama].get('no_telp','No telepon tidak ada'))
        print("email      = ",kontak[nama].get('email','Email tidak ada'))
        print()




def menu():
    while True:
        tabel_pemilihan=int(input(f"input . [memperbarui nomer telepon = 1, memperbarui gmail = 2 , menghapus kontak = 3 , menambah kontak=4 , tampilkan data = 5] = "))
        if tabel_pemilihan not in [0,1,2,3,4,5]:
            print("input dengan benar")
        else:
            return tabel_pemilihan

while True:
    pilihan=menu()
    if pilihan==0:
         print("program selesai")
         break
    elif pilihan==1:
         perbarui_no_telepon()
    elif pilihan==2:
         perbarui_email()
    elif pilihan==3:
         menghapus()
    elif pilihan==4:
         menambah_kontak()
         print(kontak)
    elif pilihan==5:
         output_data()
