# List untuk menyimpan data pengguna yang terdaftar
users = [["-"]]

# Data fasilitas yang tersedia dalam bentuk dictionary
data_fasilitas = {
    1: {'fasilitas': 'kamar berAC', 'harga': 1500000},
    2: {'fasilitas': 'kamar biasa', 'harga': 1000000},
    3: {'fasilitas': 'kamar VVVIP', 'harga': 5000000}
}

rating = ["-"] 

# nama,fasilitas,status
pesanan = [[],[],[]]
penghuni = [[],[],[]]

#warna
hijau = "\033[92m"
merah = "\033[91m"
biru = "\033[38;2;0;255;255m"
kuning = "\033[33m"
putih = "\033[0m"
orange = "\033[38;5;214m"

def login(admin_login):
    while True:
        global penghuni_sekarang

        username = input(f"{putih}masukan username : {biru}").strip().replace(" ", "").lower()
        password = input(f"{putih}masukan password : {biru}").strip().replace(" ", "").lower()

        if (username, password) == admin_login: 
            print("\033c", end="")        
            print(f"{hijau}Berhasil login sebagai admin{putih}\n")
            menu_admin()  # Memanggil menu_admin setelah login berhasil
            return
            
        else:
            for i in range(len(users)):
                if username == users[i][0] and password == users[i][1]:
                    print("\033c", end="")
                    print(f"{hijau}Berhasil Login sebagai user \nHallo {username} Selamat datang{putih}\n")
                    penghuni_sekarang = username
                    setting_penghuni_menu()  # Memanggil setting_penghuni_menu setelah login user berhasil
                    return
            print("\033c", end="")                
            print(f"""{kuning}Username atau password salah{putih}
1. Coba Lagi
2. Kembali
""")
            pilihan = input("Masukan Pilihan : ")
            if pilihan == "1": 
                print("\033c", end="")
                print(f"{biru}===== Login ====={putih}\n") 
                continue
            elif pilihan == "2":
                return
            else:
                while True:
                    print("\033c", end="")
                    print(f"""{kuning}Maaf Input Salah, Pilihan hanya 1-2{putih}
1. Coba Lagi
2. Kembali
""")
                    pilihan = input("Masukan Pilihan : ")
                    if pilihan == "1":
                        print("\033c", end="")
                        print(f"{biru}===== Login ====={putih}\n")
                        break
                    elif pilihan == "2":
                        return

def register():
    x = True
    while x:
        while True:
            username = input(f"{putih}masukan username : {biru}").strip().replace(" ", "").lower()
            if len(username) > 15:
                print("\033c", end="")
                print(f"\n{merah}Input terlalu panjang, Maksimal 15 karakter{putih}")
                continue
            elif username.isalnum():
                pass
            else:
                print("\n\033[91mUsername Tidak diperbolehkan menggunakan special karakter\033[0m")
                continue
            break
        
        while True:
            password = input(f"{putih}masukan password : {biru}").strip()
            if not password:  # Jika password kosong
                print(f"\n{merah}Password tidak boleh kosong!{putih}")
                continue
            break

        for i in range(len(users)):
            if username == users[i][0] or username == "admin":
                print("\033c", end="")
                print(f"\n{merah}Maaf Username yang anda pilih sudah digunakan, silahkan memasukan username baru{putih}")  
                break        
            elif i == len(users) - 1:
                x = False
    rating.append("-") 
    user = [username,password]
    users.append(user)
    print("\033c", end="")
    print(f"{hijau}Register berhasil{putih}")

# Fungsi untuk menampilkan menu login
def menu_login():
    while True:
        print(f"""{biru}
                        {kuning}---------------------------{biru}
                /|  /|  {kuning}|    {putih} KOS SUPRA-SUPRI     {kuning}|{biru}  
                ||__||  {kuning}|-------------------------|{biru}
               /   O O\\__       {putih}1. Login          {kuning}|{biru}
              /          \\      {putih}2. Register       {kuning}|{biru}
             /      \\     \\     {putih}3. {merah}Keluar         {kuning}|{biru}
            /   _    \\     \\ {kuning}----------------------{biru}
           /    |\\____\\     \\      {kuning}||{biru}
          /     | | | |\\____/      {kuning}||{biru}
         /       \\| | | |/ |     __{kuning}||{biru}
        /  /  \\   -------  |_____| {kuning}||{biru}
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \\----
       /\\                  |
      / /\\        |        /
     / /  |       |       |
 ___/ /   |       |       |
|____/    c_c_c_C/ \\C_c_c_c
              {putih}""")
        
        pilihan_menu = input(f"Masukkan pilihan : {biru}")
        if pilihan_menu == "1":
            print("\033c", end="")
            print(f"{biru}===== Login ====={putih}\n")
            login(("admin", "admin"))
            
            
        elif pilihan_menu == "2":
            register()

        elif pilihan_menu == "3":
            print(f"\n{biru}keluar dari sistem{putih}\n")
            return
            
        else :
            print("\033c", end="")
            print(f"\n{kuning}Pilihan tidak valid{putih}")

# Fungsi untuk menampilkan menu admin
def menu_admin():
    while True:
        print(f"""{biru}==========================
|      {putih}Menu Ibu Kos{biru}      |
==========================
|  {putih} 1. Manage Kamar {biru}     |    
|  {putih} 2. Manage Penghuni {biru}  |
|  {putih} 3. Lihat Pemesan {biru}    |
|  {putih} 4. Lihat Rating {biru}     |
|  {putih} 5. Manage Account {biru}   |
|  {putih} 6. {merah}Keluar{biru}            |
=========================={putih}
        """)
        menu = input("Pilih Menu : ")
        if menu == '1':
            print("\033c", end="")
            manage_kamar()

        elif menu == '2':
            print("\033c", end="")
            manage_penghuni()
            
        elif menu == '3':
            print("\033c", end="")
            lihat_pemesan()
            
        elif menu == '4':
            print("\033c", end="")
            lihat_rating()
            
        elif menu == '5':
            print("\033c", end="")
            manage_account()

        elif menu == '6':
            print("\033c", end="")
            print(f"{hijau}Anda telah Logout Dari Ibu Kos{putih}")
            return
        
        else :
            print("\033c", end="")
            print(f"{kuning}Pilihan tidak valid{putih}\n")
            menu_admin()
 
# Fungsi untuk menampilkan menu penghuni
def setting_penghuni_menu():
    while True:
        print(f"""{biru}===========================
|     {putih} Menu Penghuni {biru}     |
===========================
|   {putih} 1. Lihat Kamar {biru}      |
|   {putih} 2. Pesan Kamar {biru}      |
|   {putih} 3. Berikan Rating {biru}   |
|   {putih} 4.{merah} Keluar  {biru}          |
==========================={putih}
            """
        )

        x = False
        for i in range(len(pesanan)):
            for indeks_pesanan in range(len(pesanan[i])):
                if penghuni_sekarang in pesanan[i][indeks_pesanan]:
                    print(f"{biru}Status : {kuning}Menunggu Konfirmasi{putih}")
                    x = True
                    break
            if x == True:
                break
            
        x = False
        for i in range(len(penghuni)):
            for indeks_pesanan in range(len(penghuni[i])):
                if penghuni_sekarang == penghuni[i][indeks_pesanan][0]:
                    print(f"{biru}Status : {hijau}DiKonfirmasi{putih}")
                    print(f"{hijau}Anda sudah menjadi penghuni kos supra-supri{putih}")
                    x = True
                    break
            if x == True:
                break
                    
        menu_penghuni = input("Pilih Menu : ")

        if menu_penghuni == '1':
            print("\033c", end="")
            lihat_kamar()
            
        elif menu_penghuni == '2':
            print("\033c", end="")
            lihat_kamar()
            pesan_kamar()

        elif menu_penghuni == '3':
            print("\033c", end="")
            memberikan_rating()

        elif menu_penghuni == '4':
            print("\033c", end="")
            print("Keluar dari menu penghuni.")
            break
        else:
            print("\033c", end="")
            print(f"{kuning}Pilihan tidak valid{putih}\n")
                   
def manage_kamar():
    while True:
        print(f"""{biru}==========================
|     {putih} Manage kamar {biru}     |
==========================
|    {putih} 1. Lihat Kamar {biru}    |
|    {putih} 2. Tambah Kamar {biru}   |
|    {putih} 3. Edit Kamar {biru}     |
|    {putih} 4. Hapus Kamar {biru}    |
|    {putih} 5. {merah}Kembali {biru}        |
=========================={putih}
        """)
        pilihan = input("Pilih Menu: ")
        if pilihan == "1":
            print("\033c", end="")
            lihat_kamar()
        elif pilihan == "2":
            print("\033c", end="")
            tambah_kamar()
        elif pilihan == "3":
            print("\033c", end="")
            lihat_kamar()
            edit_kamar()
        elif pilihan == "4":
            print("\033c", end="")
            hapus_kamar()
        elif pilihan == "5":
            print("\033c", end="")
            return
        else:
            print("\033c", end="")
            print(f"{kuning}Pilihan tidak valid{putih}\n")
def manage_account():
    while True:
        print(f"""{biru}==========================
|    {putih} Manage Account {biru}    |
==========================
|  {putih} 1. Lihat Akun {biru}       |
|  {putih} 2. Tambah Akun {biru}      |
|  {putih} 3. Hapus Akun {biru}       |
|  {putih} 4.{merah} Kembali {biru}          |
=========================={putih}
        """) 
    
        pilihan = input("Masukan pilihan : ") 
        
        if pilihan == "1":
            print("\033c", end="")
            lihat_account()
            
        elif pilihan == "2":
            print("\033c", end="")
            print(f"{biru}===== Tambah Account =====\n")
            register()
            
        elif pilihan == "3":
            print("\033c", end="")
            lihat_account()
            hapus_account()
        
        elif pilihan == "4":
            print("\033c", end="")
            return
        else:
            print("\033c", end="")
            print(f"{kuning}input invalid{putih}")
        
                        
def manage_penghuni():
    while True:
        print(f"""{biru}==========================
|    {putih} Manage Penghuni {biru}   |
==========================
|  {putih} 1. Lihat Penghuni {biru}   |
|  {putih} 2. Tambah Penghuni {biru}  |
|  {putih} 3. Hapus Penghuni {biru}   |
|  {putih} 4.{merah} Kembali {biru}          |
=========================={putih}
        """)    
        pilihan = input("Pilih Menu: ")
        if pilihan == "1":
            print("\033c", end="")
            lihat_penghuni()
        elif pilihan == "2":
            print("\033c", end="")

            lihat_pemesan()
        elif pilihan == "3":
            print("\033c", end="")
            lihat_penghuni()
            hapus_penghuni()
        elif pilihan == "4":
            print("\033c", end="")
            return
        else:
            print("\033c", end="")
            print(f"{kuning}Pilihan tidak valid{putih}\n")            

def lihat_kamar():
    #Menghitung panjang maksimum untuk ID
    panjang_maks_id = 0
    for x in data_fasilitas.keys():
        panjang_sekarang = len(str(x))
        if panjang_sekarang > panjang_maks_id:
            panjang_maks_id = panjang_sekarang

    # Menghitung panjang maksimum untuk fasilitas
    panjang_maks_fasilitas = 0
    for x in data_fasilitas.values():
        panjang_sekarang = len(x['fasilitas'])
        if panjang_sekarang > panjang_maks_fasilitas:
            panjang_maks_fasilitas = panjang_sekarang

    # Menghitung panjang maksimum untuk harga
    panjang_maks_harga = 0
    for nilai_dalam_fasilitas in data_fasilitas.values():
        panjang_harga_sekarang = len(f"{nilai_dalam_fasilitas['harga']:,}")
        if panjang_harga_sekarang > panjang_maks_harga:
            panjang_maks_harga = panjang_harga_sekarang

    # Membuat panjang maksimum menjadi genap
    if panjang_maks_id % 2 != 0:
        panjang_maks_id += 1
    if panjang_maks_fasilitas % 2 != 0:
        panjang_maks_fasilitas += 1
    if panjang_maks_harga % 2 != 0:
        panjang_maks_harga += 1

    tabel = f"{biru}|{putih} {'ID'.center(panjang_maks_id)} {biru}| {putih}{'Fasilitas'.center(panjang_maks_fasilitas)} {biru}| {putih}{'Harga'.center(panjang_maks_harga)} {biru}|{putih}"

    print(f"{biru}=" * (len(tabel) - 84))
    print(tabel)
    print(f"{biru}=" * (len(tabel) - 84))

    # Menampilkan data dalam tabel
    for id, item in data_fasilitas.items():
        fasilitas = item['fasilitas'].ljust(panjang_maks_fasilitas,)
        harga = f"{item['harga']:,}".ljust(panjang_maks_harga)
        print(f"{biru}| {putih}{str(id).ljust(panjang_maks_id)} {biru}| {putih}{fasilitas} {biru}| {putih}{harga} {biru}|{putih}")
    print(f"{biru}=" * (len(tabel) - 84),f"{putih}\n")
   
# Fungsi rekursif untuk menambahkan kamar
def tambah_kamar():
    kamar_id = len(data_fasilitas) + 1
    print("\033c", end="")
    print(f"{biru}===== Tambah Kamar ====={putih}\n")
    # Validasi input nama kamar
    while True:
        nama_kamar = input("Masukkan nama kamar : ").strip()
        try:
            for char in nama_kamar:
                if not (char.isalpha() or char == ' '):
                    raise ValueError(f"{merah}Input hanya boleh berisi alfabet dan spasi.{putih}")

            teks_bersih = ' '.join(nama_kamar.split())
            jumlah_kata = len(teks_bersih.split())
            if jumlah_kata > 30:
                raise ValueError(f"{merah}Input tidak boleh lebih dari 30 kata, saat ini ada {jumlah_kata} kata.{putih}")
        except ValueError as error:
            print("\033c", end="")
            print(f"{biru}===== Tambah Kamar ====={putih}\n")
            print(f"{error}")
            continue
        if not nama_kamar: 
            print(f"{merah}Nama kamar tidak boleh kosong!{putih}\n")
        else:
            break
   
    # Validasi input harga kamar
    while True:
        try:
            harga_kamar = int(input("Masukkan harga kamar : "))
            if harga_kamar < 0:  # Jika harga negatif
                print(f"{merah}Harga kamar tidak boleh negatif!{putih}\n")
            else:
                break
        except ValueError:  # Jika input bukan angka
            print("\033c", end="")
            print(f"{biru}===== Tambah Kamar ====={putih}\n")
            print(f"{merah}Input hanya berupa angka!{putih}\n")    
            
    data_fasilitas[kamar_id] = {'fasilitas': nama_kamar, 'harga': harga_kamar}
    pesanan.append([])
    penghuni.append([])
    print(f"\n{hijau}Kamar berhasil ditambahkan!{putih}")
    
    # Meminta pengguna menambah kamar lain atau kembali
    lanjut = input(f"\nTambah kamar lain? ({hijau}y{putih}/{merah}n{putih}): ").lower()
    if lanjut == 'y':
        print("\033c", end="")
        tambah_kamar()  # Rekursif untuk menambah kamar lain 
    elif lanjut == 'n':
        print("\033c", end="") 
        return
    else:
        print("\033c", end="") 
        print(f"{kuning}Input invalid{putih}") 
        return   
           
def edit_kamar():
    while True:
        try:
            pilihan = int(input("Masukan id yang ingin di edit : "))
            break
        except ValueError:
            print("\033c", end="")
            lihat_kamar()
            print(f"{kuning}Input hanya angka{putih}")
    for key in data_fasilitas:
        if pilihan == key:
            while True:
                nama_baru = input("Masukkan nama kamar baru: ").strip()
                try:
                    for char in nama_baru:
                        if not (char.isalpha() or char == ' '):
                            raise ValueError(f"{merah}Input hanya boleh berisi alfabet dan spasi.{putih}")

                    teks_bersih = ' '.join(nama_baru.split())
                    jumlah_kata = len(teks_bersih.split())
                    if jumlah_kata > 30:
                        raise ValueError(f"{merah}Input tidak boleh lebih dari 30 kata, saat ini ada {jumlah_kata} kata.{putih}")
                except ValueError as error:
                    print("\033c", end="")
                    print(f"{biru}===== Edit Kamar ====={putih}\n")
                    print(f"{error}")
                    continue
                if not nama_baru: 
                    print(f"{merah}Nama kamar tidak boleh kosong!{putih}\n")
                else:
                    break
            
            while True:
                try:
                    harga_baru = int(input("Masukkan harga kamar baru : "))
                    if harga_baru < 0:  # Jika harga negatif
                        print(f"{kuning}Harga kamar tidak boleh negatif!{putih}\n")
                    elif harga_baru <= 100000:
                        print(f"{kuning}Harga kamar terlalu murah!{putih}\n")
                        
                    else:
                        
                        break
                except ValueError:  # Jika input bukan angka
                    print("\033c", end="")
                    print(f"{biru}===== Edit Kamar ====={putih}\n")
                    print(f"{merah}Input hanya berupa angka!{putih}\n")
            
            data_fasilitas[key]['fasilitas'] = nama_baru
            data_fasilitas[key]['harga'] = harga_baru
            print(f"{hijau}Kamar berhasil diedit{merah}\n")
            return
        
    else:
        print("\033c", end="")
        print(f"{kuning}ID kamar tidak ditemukan{putih}")
        return
            
def pesan_kamar():
    global penghuni
    for indeks_penghuni in range(len(penghuni)):
        for indeks_dalam in range(len(penghuni[indeks_penghuni])):
            if penghuni_sekarang == penghuni[indeks_penghuni][indeks_dalam][0]:   
                print(f"{biru}kamu sudah Diterima menjadi penghuni{putih}")
                print(f"Apakah kamu mau membatalkan kamar\n")
                print(f"""\n{biru}Batalkan kamar
{putih}1. Batalkan Kamar
2. {merah}Kembali{putih}
""")
                pilihan = input("Masukan pilihan : ")
                if pilihan == "1":
                    print("\033c", end="")
                    print(f"{hijau}Kamar berhasil dibatalkan{putih}")
                    del penghuni[indeks_penghuni][indeks_dalam]
                    return
                elif pilihan == "2":
                    print("\033c", end="")
                    return 
                
                else:
                    print("\033c", end="")
                    print(f"{kuning}input invalid{putih}") 
                    return

    for i in range(len(pesanan)):
        for indeks_pesanan in range(len(pesanan[i])):
            if penghuni_sekarang == pesanan[i][indeks_pesanan][0]:
                print(f"{kuning}Maaf Pengguna hanya dapat memesan 1 kamar saja\n{biru}anda dapat membatalkan pesanan kamar anda dan memilih kamar baru{putih}")
                print(f"""\n{biru}Pesan Kamar
{putih}1. Batalkan Kamar
2. {merah}Kembali{putih}
""")
                pilihan = input("Masukan pilihan : ")
                if pilihan == "1":
                    print("\033c", end="")
                    print(f"{hijau}Kamar berhasil dibatalkan{putih}")
                    del pesanan[i][indeks_pesanan]
                    return
                elif pilihan == "2":
                    print("\033c", end="")
                    return 
                
                else:
                    print("\033c", end="")
                    print(f"{kuning}input invalid{putih}") 
                    return   
        
    while True:
        try:
            id_kamar = int(input("Masukkan ID kamar yang ingin dipesan : ")) 
            break
        except ValueError:
            print("\033c", end="")
            lihat_kamar()
            print(f"{merah}Input Hanya Berupa Angka{putih}")
            
    if id_kamar in data_fasilitas:
        for indeks_fasilitas in range(len(data_fasilitas)):
            if id_kamar == indeks_fasilitas + 1:
                pesanan_baru = [penghuni_sekarang,data_fasilitas[id_kamar]["fasilitas"], "Belum Dikonfirmasi"]
                pesanan[indeks_fasilitas].append(pesanan_baru)
                break
        print("\033c", end="")                  
        print(f"{hijau}{data_fasilitas[id_kamar]['fasilitas']} berhasil dipesan!{putih}\n")
    else:
        print("\033c", end="")
        print(f"{kuning}ID kamar tidak ditemukan.{putih}\n")
        
# Prosedur untuk menghapus kamar berdasarkan ID
def hapus_kamar():
    lihat_kamar()
    while True:
        try:
            id_kamar = int(input("Masukkan ID kamar yang ingin dihapus : "))
            break
        except ValueError:
            print("\033c", end="")
            print(f"{merah}Input Hanya Berupa Angka{putih}\n")
            lihat_kamar()
    if id_kamar in data_fasilitas:
        kamar = data_fasilitas.pop(id_kamar)
        print("\033c", end="")
        print(f"{hijau}{kamar['fasilitas']} berhasil dihapus.{putih}\n")
    else:
        print("\033c", end="")
        print(f"{kuning}Fasilitas tidak ditemukan.{putih}\n")

# Prosedur untuk menampilkan daftar pengguna
def lihat_penghuni():
    gak_ada_indeks = 0
    for a in range(len(penghuni)):
        if not penghuni[a]:
            gak_ada_indeks += 1
            
    if gak_ada_indeks == len(penghuni):
        print(f"{kuning}Tidak ada Penghuni yang tersedia.{putih}\n")
        return
    else :
        tabel(penghuni,0) 

# Prosedur untuk menghapus penghuni
def hapus_penghuni():
    ga_ada_indeks = 0
    for x in range(len(penghuni)):
        if not penghuni[x]:
            ga_ada_indeks += 1
            
    if ga_ada_indeks == len(penghuni): 
        print("\033c", end="")
        print(f"{kuning}Tidak ada penghuni yang terdaftar{putih}") 
        return     
    while True:
        try:
            pilihan = int(input("Masukan Plihan : "))
            break
        except ValueError:
            print("Input yang anda masukkan bukan angka")
    if pilihan >= len(penghuni) or pilihan <= 0:
        print("\033c", end="")
        print(f"{kuning}ID Penghuni Tidak ditemukan{putih}\n")
        return
    else:
        p = False
        for i in range(len(penghuni)):
            for indeks_penghuni in range(len(penghuni[i])):
                if id_nama_list[pilihan -1] == penghuni[i][indeks_penghuni][0]:
                    del penghuni[i][indeks_penghuni]
                    del id_nama_list[pilihan -1]
                    p = True
                    break
            if p == True:
                break       
   
            

def lihat_account():
    global id_nama_list_account
    panjang_maks_id = 2
    panjang_maks_nama = 4
    panjang_maks_password = 8
    
    for i in range(1,len(users)):
        panjang_nama = len(users[i][0])
        panjang_password = len(users[i][1])
        
        if panjang_nama > panjang_maks_nama:
            panjang_maks_nama = panjang_nama
        if panjang_password > panjang_maks_password:
            panjang_maks_password = panjang_password
    
    panjang_id = len(str(len(users )-1))
    
    if panjang_id > panjang_maks_id:
        panjang_maks_id = panjang_id
    if panjang_maks_id % 2 != 0:
        panjang_maks_id += 1
    if panjang_maks_nama % 2 != 0:
        panjang_maks_nama += 1
    if panjang_maks_password % 2 != 0:
        panjang_maks_password += 1
        
    if len(users) > 1 :      
        tabels = f"| {'ID'.center(panjang_maks_id)} | {'Nama'.center(panjang_maks_nama)} | {'password'.center(panjang_maks_password)} |"
        print(f"{biru}="* len(tabels),f"{putih}") 
        print(tabels)
        print(f"{biru}="* len(tabels),f"{putih}") 
        
        id = 1
        id_nama_list_account = []
        for i in range(1,len(users)):
            if len(users) == 1:
                continue
            else:
                print(f"| {str(id).ljust(panjang_maks_id)} | {users[i][0].ljust(panjang_maks_nama)} | {users[i][1].ljust(panjang_maks_password)} |")
                id += 1
                id_nama_list_account.append(users[i][0])
        
        print("="* len(tabels),"\n")
    
    else: 
        print(f"{kuning}Tidak ada account yang tersedia{putih}\n")

def hapus_account():
    global id_nama_list_account
    x = True
    while x:
        if len(users) == 1:
            print("\033c", end="")
            print(f"T{kuning}idak ada Account yang terdaftar{putih}\n")
            return

        else:
            print(f"\n{biru}===== Hapus Account ====={putih}")
            pilihan = int(input("Masukan ID yang ingin dihapus : "))
            for i in range(1,len(users)):
                if pilihan > (len(users)-1) or pilihan <= 0 :
                    print("\033c", end="")
                    print(f"{kuning}Input invalid{putih}\n")
                    return
                
                elif id_nama_list_account[pilihan -1] == users[i][0]:
                    print("\033c", end="")
                    print(f"{hijau}Account dengan nama {users[i][0]} telah dihapus{putih}")
                    del rating[pilihan] 
                    del id_nama_list_account[pilihan -1]                       
                    x = False
     
                    for j in range(len(pesanan)):
                        for indeks in range(len(pesanan[j])):
                            if pesanan[j][indeks][0] == users[i][0]:
                                del pesanan[j][indeks]
                                del users[i]
                                x = True
                                break
                        if x == True: 
                            break
                    
                    for j in range(len(penghuni)):
                        for indeks in range(len(penghuni[j])):
                            if penghuni[j][indeks][0] == users[i][0]:
                                del penghuni[j][indeks]
                                del users[i]
                                x = True
                                break
                        if x == True: 
                            break
                    if x == False:    
                        del users[i]
                    return 
            
                
      
def memberikan_rating():
    for x in range(1,len(users)):
        if users[x][0] == penghuni_sekarang:
            print("\033c", end="")
            print(f"{biru}===== Rating ====={putih}\n")
            while True:
                print(f"{biru}Berikan rating Untuk Kos-kosan{putih}")
                try:
                    hasil_rating = int(input("Rating (1-5) : "))
                except ValueError:
                    print("\033c", end="")
                    print(f"{biru}===== Rating ====={putih}\n")
                    print(f"{merah}input Invalid{putih}\n")
                    continue
                if hasil_rating > 5 or hasil_rating < 1:
                    print("\033c", end="")
                    print(f"{biru}===== Rating ====={putih}\n")
                    print(f"{kuning}Berikan Rating hanya (1-5){putih}\n")
                    continue
                break
            
            print("\033c", end="")
            print(f"{hijau}Rating Telah Diberikan, Terima Kasih{putih}\n")
            rating[x] = hasil_rating

def lihat_rating():
    total_rating = 0
    users_rating = 0

    for x in range(1,len(users)):
        if rating[x] == "-":
            continue
        users_rating += 1
        total_rating += rating[x]
        #print(f"{users[x][0]} : {rating[x]}")
    if users_rating == 0:
        print(f"{kuning}tidak ada yang memberi rating kos-kosan anda{putih}\n")
    else:
        nilai_rata2 = total_rating / users_rating  
        print(f"{biru}Nilai rata-rata rating kos anda : {nilai_rata2:.1f}{putih}\n") 
        for i in range(int(nilai_rata2)):
            print(f"{kuning}★{putih}", end= " ")
        print("\n")
 
# misal masing masing maks 3           
def lihat_pemesan():
    global cek_tabel
    cek_tabel = 1
    while True:
        gak_ada_indeks = 0
        for a in range(len(pesanan)):
            if not pesanan[a]:
                gak_ada_indeks += 1
                
        if gak_ada_indeks == len(pesanan):
            print(f"{kuning}Tidak ada pengguna yang memesan kamar.{putih}\n")
            return
        else :
            if cek_tabel == 1:
                tabel(pesanan,1)
            
        print(f"""{biru}Menerima penghuni
{putih}1. Konfirmasi
2. Batalkan
3. {merah}kembali{putih}""")
        
        pilihan = input("\nMasukan Pilihan :")
           
        if pilihan == "1":
            konfirmasi_atau_batalkan(1)   
                                                                     
        elif pilihan == "2":
            konfirmasi_atau_batalkan(0)
                                
        elif pilihan == "3":
            print("\033c", end="")
            return
        
        else:
            print("\033c", end="")
            tabel(pesanan,1)
            print(f"{kuning}Pilihan tidak valid{putih}\n")
            cek_tabel = 0

# jika indeks = 1 maka konfirmasi
def konfirmasi_atau_batalkan(indeks):
    global cek_tabel
    ketemu_nama = False
    id_pengguna = int(input("Masukan id Pengguna : "))
    if id_pengguna > len(id_nama_list) or id_pengguna <= 0 :
        print("\033c", end="")
        tabel(pesanan,1)
        print(f"{kuning}ID tidak ditemukan{putih}\n")
        cek_tabel = 0

    else:
        for i in range(len(pesanan)):
            for indeks_pesanan in range(0,len(pesanan[i])):
                
                if id_nama_list[id_pengguna - 1] == pesanan[i][indeks_pesanan][0]: 
                    if indeks == 1:                    
                        penghuni[i].append(pesanan[i][indeks_pesanan])
                        penghuni[i][(len(penghuni[i])-1)][2] = "Dikonfirmasi"
                    print("\033c", end="")                          
                    nama_tampungan = pesanan[i][indeks_pesanan][0] 
                    del pesanan[i][indeks_pesanan]
                    del id_nama_list[id_pengguna -1]
                    cek_tabel = 0
                    ketemu_nama = True
                    if len(pesanan[i]) > 0:
                        tabel(pesanan,1)
                         
                    if indeks == 1:                          
                        print(f"{hijau}{nama_tampungan} Berhasil ditambahkan menjadi penghuni{putih}\n")
                    else:
                        print(f"{hijau}{nama_tampungan} Berhasil Dibatalkan{putih}\n")
                    break   
            if ketemu_nama == True:
                break        
             
def tabel(penghuni_atau_pesanan,cek):
    global panjang_maks_id, panjang_maks_nama, panjang_maks_fasilitas, panjang_maks_status, tabels, id_nama_list
    
    panjang_maks_id = 2
    panjang_maks_nama = 4
    panjang_maks_fasilitas = 9
    panjang_maks_status = 6
    
    panjang_id = 0
    for i in range(len(penghuni_atau_pesanan)):
        for indeks_pesanan in range(len(penghuni_atau_pesanan[i])):
            panjang_nama = len(penghuni_atau_pesanan[i][indeks_pesanan][0])
            panjang_fasilitas = len(penghuni_atau_pesanan[i][indeks_pesanan][1])
            panjang_status = len(penghuni_atau_pesanan[i][indeks_pesanan][2])

            if panjang_nama > panjang_maks_nama:
                panjang_maks_nama = panjang_nama
            if panjang_fasilitas > panjang_maks_fasilitas:
                panjang_maks_fasilitas = panjang_fasilitas
            if panjang_status > panjang_maks_status:
                panjang_maks_status = panjang_status
        
        panjang_id += len(penghuni[i])
    
    if panjang_id > panjang_maks_id:
        panjang_maks_id = len(str(panjang_id))
        
    if panjang_maks_id % 2 != 0:
        panjang_maks_id += 1
    if panjang_maks_nama % 2 != 0:
        panjang_maks_nama += 1
    if panjang_maks_fasilitas % 2 != 0:
        panjang_maks_fasilitas += 1
    if panjang_maks_status % 2 != 0:
        panjang_maks_status += 1
        
    # mengecek setiap kamar         
    tabels = f"{biru}| {putih}{'ID'.center(panjang_maks_id)} {biru}| {putih}{'Nama'.center(panjang_maks_nama)} {biru}| {putih}{'Fasilitas'.center(panjang_maks_fasilitas)} {biru}|{putih} {'Status'.center(panjang_maks_status)} {biru}|{putih}"
    print(f"{biru}=" * (len(tabels) - 105 ))
    print(tabels)
    print(f"{biru}=" * (len(tabels) - 105))
    
    id = 1
    id_nama_list = []
    for x in range(len(penghuni_atau_pesanan)):
        for indeks_pesanan in range(len(penghuni_atau_pesanan[x])):
            if not penghuni_atau_pesanan[x]:
                continue
            else:
                nama = penghuni_atau_pesanan[x][indeks_pesanan][0].ljust(panjang_maks_nama)
                fasilitas = penghuni_atau_pesanan[x][indeks_pesanan][1].ljust(panjang_maks_fasilitas)
                status = penghuni_atau_pesanan[x][indeks_pesanan][2].ljust(panjang_maks_status)
                
                #masuk ke penghuni
                if cek == 0:
                    print(f"{biru}| {putih}{str(id).ljust(panjang_maks_id)} {biru}| {putih}{nama} {biru}| {putih}{fasilitas} {biru}| {hijau}{status} {biru}|{putih}")
                    
                #masuk ke pesanan
                elif cek == 1 :
                    print(f"{biru}| {putih}{str(id).ljust(panjang_maks_id)} {biru}| {putih}{nama} {biru}|{putih} {fasilitas} {biru}| {kuning}{status} {biru}|{putih}")
                    
                id += 1
                id_nama_list.append(penghuni_atau_pesanan[x][indeks_pesanan][0])
    print(f"{biru}=" * (len(tabels) - 105), f"{putih}\n")
            
# Memulai program dengan menu login
print(f"""{biru} _  __              ____                                  ____                   _ 
| |/ /___  ___     / ___| _   _ _ __  _ __ __ _          / ___| _   _ _ __  _ __(_)
| ' // _ \\/ __|    \\___ \\| | | | '_ \\| '__/ _` |  _____  \\___ \\| | | | '_ \\| '__| |
| . \\ (_) \\__ \\     ___) | |_| | |_) | | | (_| | |_____|  ___) | |_| | |_) | |  | |
|_|\\_\\___/|___/    |____/ \\__,_| .__/|_|  \\__,_|         |____/ \\__,_| .__/|_|  |_|
                               |_|                                   |_|           """)
   
print(f"""
{orange}            _                        _                        _{putih} 
{orange}          _|=|__________           _|=|__________           _|=|__________{putih}
{orange}         /              \\         /              \\         /              \\ {putih}
{orange}        /                \\       /                \\       /                \\ {putih}
{orange}       /__________________\\     /__________________\\     /__________________\\ {putih}
{putih}        ||  || /--\\ ||  ||       ||  || /--\\ ||  ||       ||  || /--\\ ||  ||    {putih}
{putih}        ||[]|| | .| ||[]||       ||[]|| | .| ||[]||       ||[]|| | .| ||[]||{putih}
{putih}      ()||__||_|__|_||__||()   ()||__||_|__|_||__||()   ()||__||_|__|_||__||() {putih}
{putih}     ( )|-|-|-|====|-|-|-|( ) ( )|-|-|-|====|-|-|-|( ) ( )|-|-|-|====|-|-|-|( ) {putih}
{hijau}     ^^^^^^^^^^{putih}===={hijau}^^^^^^^^^^ ^^^^^^^^^^{putih}===={hijau}^^^^^^^^^^ ^^^^^^^^^^{putih}===={hijau}^^^^^^^^^^ {putih}""")

menu_login()