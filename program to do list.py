import os 
import csv 
import termcolor 

def clear ():
    os.system("cls")

def garis ():
    print ("="*50)
def garis2 ():
    print ("-"*50)

def cover ():
    garis()
    print ("PROGRAM TO DO LIST".center(50))
    garis2()

def enter():
    enter = input ("tekan [ENTER] untuk melanjutkan program ...")

def menu (): #membuat fungsi dengan nama menu
    clear() #memanggil fungsi clear
    cover () #memanggil fungsi cover
    print ("REGISTRASI DAN LOGIN".center(50))
    garis() 
    print ("""
                1. REGISTRASI
                2. LOGIN
""") #mencetak registrasi dan login 
    garis() #memanggil fungsi garis
    while True : #perulangan jika kondisi True
        try : #melakukan sebuah percobaan
            pilih = int (input ("Pilih Opsi yang tersrdia >> ")) #inputan opsi yang dipilih 
            if pilih == 1 : #jika inputan user 1 
                enter() #memanggil fungsi enter 
                registrasi() #memanggil fungsi registrasi
                break #menghentikan pengulangan
            elif pilih == 2 : #jika inputan user 2 
                enter() #memanggil fungsi enter
                login () #memanggil fungsi login
                break #menghentikan perulangan 
            else : #input selain 1 dan 2  
                print ("Opsi yang anda pilih tidak tersedia") #mencetak kalimat 
        except ValueError : #apabila terdapat error 
            termcolor.cprint ("masukkan input dalam bentuk angka", "red") #mencetak kalimat dengan warna merah
            enter() #memanggil fungsi enter
            menu () #memanggil fungsi menu 
            

def penampung (): #membuat fungsi dengan nama penampung 
    global datauser, list_password, list_username #menjadikan variabel lokal menjadi global
    datauser = [] #list penampung data user
    list_username = [] #list penampung username user
    list_password = [] #list penampung password
    with open ("datauser.csv", mode = "r") as file : #membuka file csv dengan nama datauser.csv
        csv_reader = csv.reader(file) #method csv untuk membaca file 
        for row in csv_reader:  #perulangan untuk membaca setiap baris pada file csv
            datauser.append(row)  #menambahkan data pada list datauser

    for i in range  (len (datauser)):  #perulangan untuk mengambil data pada list datauser
        list_username.append(datauser[i][0])  #menambahkan data pada list username
        list_password.append (datauser[i][1])   #menambahkan data pada list password
    return list_username, list_password  #mengembalikan data user, username, dan password

def registrasi (): #membuat fungsi dengan nama registrasi
    clear() # memanggil  fungsi clear
    cover() #memanggil fungsi cover 
    print ("HALAMAN LOGIN".center(50))
    garis()
    list_username, list_password = penampung () # mengambil data user, username, dan password dari fungsi penampung 

    while True : # perulangan jika kondisi benar 
        while True : # perulangan jika kondisi benar 
            try : #percobaan terhadap inputan
                username = input ("buat username baru >> ") #inputan username baru yang ingin di buat user 
                if username in list_username or len (username) <4: #jika  username sudah ada pada list username 
                    raise ValueError ("Username sudah digunakan, username minimal terdiri dari 4 karakter") #menandai bahwa erorr
                else : #selain kondisi diatas 
                    break #keluar dari perulangan
                
            except ValueError as erorr:  #apabila terdapat error
                termcolor.cprint (erorr, "red") #cetak kalimat error dengan warna merah 
        while True : #perulangan jika kondisi benar 
            try : #percobaan terhadap inputan 
                password = input ("buat password baru >> ") #inputan password baru dari user 
                if password == username or len(password) < 8 : #jika pasword sama dengan username atau panjang password kurang dari 8 karakter 
                    raise ValueError ("Password harus lebih dari 8 karakter dan tidak sama dengan username") #tandai bahwa error
                else : #jika tidak memenuhi
                    break #keluar dari pengulangan 
            except ValueError as error: # apabila terindikasi error
                termcolor.cprint (error, "red") #mencetak error dengan warna merah 

        while True :  #perulangan apabila kondisi terpenuhi
            try : #percobaan terhadap inputan 
                password2 = input ("konfirmasi password anda >> ")  #input konfirmasi password user 
                if password2 != password : #jika konfirmasi password tidak sama dengan password yang dimasukkan 
                    raise  ValueError ("password yang anda masukkan tidak sama") #tandai bahwa error
                else : #jika tidak memenuhi
                    break # keluar dari perulangan 
            except ValueError as error: #apabila ada error
                termcolor.cprint (error, "red") #mencetak error dengan warna merah 

        garis() #memanggil fungsi garis 
        with open ("datauser.csv", mode = "a", newline = "\n") as file : # membuka file csv dengan nama datauser.csv dalam mode menulis 
            border = ["username", "password"] #borderr dari file csv 
            writer = csv.DictWriter (file, fieldnames=border) #method  csv untuk menulis file csv 
            writer.writerow ( {"username" : username, "password" : password2} ) #memasukkan  data user ke dalam file csv 
        termcolor.cprint ("registrasi berhasil, silahkan login", "green") #mencetak  kalimat registrasi berhasil dengan warna hijau 
        enter() #memanggil fungsi enter
        menu() #memanggil fungsi menu 
        
def login (): #membuat fungsi dengan nama login 
    clear () #memanggil fungsi clear
    cover () #memanggil  fungsi cover
    print ("HALAMAN LOGIN".center(50))
    garis()
    global username
    list_username, list_password = penampung () #mengambil nilai dari fungsi penampung 
    username = input ("masukkan username anda >> ") #inputan username user 
    password = input ("masukkan password anda >> ") #inputan password user 
    a = 0 #penanda
    for i in range (len(list_username)): #perulangan sebagai index
        if username == list_username[i] and password == list_password[i] : #jika username dan password terdapat pada indeks yang sama 
            a += 1 #penanda menjadi 1 
    if a == 1 : #jika penanda 1 
        termcolor.cprint ("login berhasil", "green") #mencetak login berhasil berwarna hijau 
        enter() #memanggil fungsi enter
        main() #memanggil fungsi main
    else : #jika kondisi tidak terpenuhi
        termcolor.cprint ("login tidak berhasil, silahkan masukkan username dan password yang benar", "red") #mencetak login tidak berhasil berwarna merah 
        enter () #memanggil fungsi enter
        login() #memanggil fungsi login 

def main ():
    while True :
        clear()
        cover()
        print ("HALAMAN UTAMA".center(50))
        garis2()
        print (f"User : {username}".center(50))
        garis()
        print ("MENU :\n")
        print ("1. TAMBAH JADWAL")
        print ("2. LIHAT JADWAL")
        print ("3. HAPUS JADWAL")
        print ("4. KELUAR\n")
        garis()
        try :
            pilih = int (input ("silahkan pilih menu >>"))
            if pilih  == 1 :
                enter()
                tambah_jadwal()
                break
            elif pilih == 2 :
                enter()
                lihat_jadwal()
                break
            elif pilih == 3 :
                enter()
                hapus_jadwal()
                break
            elif pilih == 4 :
                exit()
                break
            else :
                raise ValueError ("opsi tidak tersedia... silahkan pilih ulang...")
        except ValueError as error:
            termcolor.cprint(error,"red")
            enter()
        
    pass
    pass
def exit ():
    try :
        yakin = input ("apakah anda yakin ingin keluar ... [y]/[n]")
        if yakin.lower() == "y":
            clear()
            termcolor.cprint ("terimakasih telah menggunakan program ini...", "green")
        elif yakin.lower() == "n":
                    main()
        else :
            raise  ValueError ("input tidak valid... silahkan pilih ulang...")
    except ValueError as error :
            termcolor.cprint(error,"red")
            enter ()
            exit ()

def tambah_jadwal():
    while True :
        clear ()
        cover ()
        print ("TAMBAH TUGAS".center(50))
        garis2()
        print (f"USER SAAT INI : {username}")
        garis()
        while True :
            try :
                tugas = input ("tugas dari mata kuliah >> ")
                if tugas == "" :
                    raise ValueError ("input tidak boleh kosong...")
                else :
                    break
            except ValueError as error :
                termcolor.cprint (error, "red")
        while True :
            try :
                deadline = input ("masukkan deadline tugas >> ")
                if deadline == "" :
                    raise ValueError ("input tidak boleh kosong...")
                else :
                    break
            except ValueError as error :
                termcolor.cprint (error, "red")
        while True :
            try :
                deskripsi = input ("deskripsi dari tugas >> ")
                if deskripsi == "" :
                    raise ValueError ("input tidak boleh kosong...")
                else :
                    break
            except ValueError as error :
                termcolor.cprint (error, "red")

        with open (f"{"user"+username +".csv"}", mode ="a", newline="\n") as file:
            border = ["tugas", "deadline", "deskripsi"]  
            writer = csv.DictWriter (file, fieldnames=border)
            writer.writerow ({"tugas" : tugas, "deadline" : deadline, "deskripsi" : deskripsi})
        garis ()
        termcolor.cprint ("tugas berhasil ditambahkan...", "green")
        lagi = input ("apakah ingin menambahkan tugas lagi ... [y]/[n]")
        if  lagi.lower() == "y":
            enter()
            continue
        else :
            enter()
            main()
            break

def lihat_jadwal():
    clear()
    cover()
    print ("LIHAT TUGAS".center(50))
    garis2()
    print (f"USER SAAT INI : {username}")
    garis()
    tampungan = []
    with  open (f"{"user"+username +".csv"}", mode ="r") as file:
        reader = csv.reader(file,delimiter =",")
        for i in reader :
            tampungan.append(i)
    for i,a in enumerate(tampungan) :
        print (f" ")
        print (f"{i + 1}. tugas mata kuliah :  {a[0]}")
        print (f"   deadline tugas    :  {a[1]}")
        print (f"   deskripsi tugas   :  {a[2]}")
    garis()
    enter ()
    main ()
        
def hapus_jadwal():
    while True :
        clear()
        cover()
        print ("HAPUS TUGAS".center(50))
        garis2()
        print (f"USER SAAT INI : {username}")
        garis()
        tampungan = []
        with  open (f"{"user"+username +".csv"}", mode ="r") as file:
            reader = csv.reader(file,delimiter =",")
            for i in reader :
                tampungan.append(i)
            for i,a in enumerate(tampungan) :
                print (f" ")
                print (f"{i + 1}. tugas mata kuliah :  {a[0]}")
                print (f"   deadline tugas    :  {a[1]}")
                print (f"   deskripsi tugas   :  {a[2]}")
            garis()
            print (tampungan)
        while True :
            try :
                hapus = int (input ("masukkan nomor tugas yang ingin dihapus >> "))
                if hapus < 1 or hapus >len(tampungan) :
                    raise ValueError ("inputan tidak valid")
                else :
                    tampungan.pop(hapus - 1)
                    break
            except ValueError as error:
                termcolor.cprint(error, "red")
                continue 
        print (tampungan)
        enter()
        with open (f"{"user"+username +".csv"}", mode ="w", newline="\n") as file:  
            writer = csv.writer (file)
            for i in range(len(tampungan)):
                writer.writerow([tampungan[i][0],tampungan[i][1],tampungan[i][2]])
            garis ()
        a = 0
        while True :
            try :
                lagi = input ("ingin menghapus lagi ?... [y]/[n]")
                if lagi.lower() == "y":
                    enter()
                    hapus_jadwal()
                    break
                elif  lagi.lower() == "n":
                    enter()
                    main()
                    break
                else :
                    raise ValueError ("inputan tidak valid")
            except ValueError as error :
                termcolor.cprint(error, "red")
                continue
    
             

if __name__ == "__main__":
    menu()