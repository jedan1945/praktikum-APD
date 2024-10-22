# Data pengguna dan koleksi gundam
users = {
    "raffi": {"password": "37", "role": "owner"}
}

gundam = {
    "freedom": {"grade": "hg", "kondisi": "dirakit"},
    "00 shia qant": {"grade": "hg", "kondisi": "dirakit"},
    "dynames huang zhong": {"grade": "sd", "kondisi": "dirakit"},
    "gundam x": {"grade": "mg", "kondisi": "mib"}  # mib = mint in box, belum dirakit
}

def login(users):
    komandan = input("Komandan: ")
    password = input("Password: ")

    if komandan in users and users[komandan]["password"] == password:
        print(f"Selamat datang, komandan {komandan}!")
        return komandan, users[komandan]["role"]
    else:
        print("Login gagal! Nama atau password salah.")
        return None, None

def register(users):
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    role = input("Masukkan role (owner/pelancong): ")

    if role in ["owner", "pelancong"]:
        users[username] = {"password": password, "role": role}
        print(f"Pengguna {username} berhasil didaftarkan.")
    else:
        print("Role tidak valid. Harus owner atau pelancong.")
    return users

# list koleksi gundam
def data_list_gundam(gundam):
    if len(gundam) == 0:
        print("Belum ada koleksi gundam.")
    else:
        print("List Koleksi Gundam:")
        for i, (nama, info) in enumerate(gundam.items()):
            print(f"{i + 1}. {nama} - grade: {info['grade']} - kondisi: {info['kondisi']}")

# menambah koleksi gundam
def tambah_gundam(gundam):
    nama = input("Masukkan nama gundam: ")
    grade = input("Masukkan grade: ")
    kondisi = input("Masukkan kondisi: ")
    gundam[nama] = {"grade": grade, "kondisi": kondisi}
    print(f"Gundam {nama} berhasil ditambahkan.")
    return gundam

# mengedit koleksi gundam
def updaate_gundam(gundam):
    data_list_gundam(gundam)
    try:
        index = int(input("Masukkan nomor gundam yang ingin diupdate: ")) - 1
        nama_gundam = list(gundam.keys())[index]

        nama_baru = input(f"Masukkan nama baru untuk {nama_gundam} (kosongkan jika tidak ingin mengubah): ")
        grade_baru = input(f"Masukkan grade baru (kosongkan jika tidak ingin mengubah): ")
        kondisi_baru = input(f"Masukkan kondisi baru (kosongkan jika tidak ingin mengubah): ")

        if nama_baru:
            gundam[nama_baru] = gundam.pop(nama_gundam)
            nama_gundam = nama_baru
        if grade_baru:
            gundam[nama_gundam]["grade"] = grade_baru
        if kondisi_baru:
            gundam[nama_gundam]["kondisi"] = kondisi_baru

        print(f"Gundam {nama_gundam} berhasil diupdate.")
    except (IndexError, ValueError):
        print("Pilihan tidak valid.")
    return gundam

# menghapus koleksi gundam
def hapus_gundam(gundam):
    data_list_gundam(gundam)
    try:
        index = int(input("Masukkan nomor gundam yang ingin dihapus: ")) - 1
        nama_gundam = list(gundam.keys())[index]
        del gundam[nama_gundam]
        print(f"Gundam {nama_gundam} berhasil dihapus.")
    except (IndexError, ValueError):
        print("Pilihan tidak valid.")
    return gundam

# menu owner
def pilihan_owner(gundam):
    while True:
        print("""
@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@ |==================================================|
@@@@@@@@@@@@@@@@@@@@@BPB&@@@@@@@@@@@#5#@@@@@ |==================================================|
@@@@@@@@@@@@&&@@@@@@@@PJ7?#@@@@@@@&G75@@@@@@ |==================================================|
@@@@@@@@@@@@@BPB&@@@@@@PJ~P&&###&@@YJ@@@#B&@ |=SELAMAT DATANG KOMANDAN, silahkan pilih menu dulu|
@@@@@@@@@@@@@@&PJJP#&BGG5?!GGGPPP##J#@#YY&@@ |= 1. tampilkan data list koleksi.                 |
@@@@@@@@@@@@@@@@GJ7!!?JY55?JBGGG5P5P#5!5@@@@ |= 2. tambah data list koleksi.                    |
@@@@@@@@@@@@@@@&G5PYJ?7!!!77JPB55Y7!!7G@@@@@ |= 3. update data koleksi.                         |
@@@@@@@@@@@@@@@&G5PPPPPP5YJ?75P55JYB&&@@@@@@ |= 4. hapus data koleksi.                          |
@@@@@@@@@@@@@@@&G5PPPB5?#75PB5Y5B@@@@@@@@@@@ |= 5. keluar dari data koleksi.                    |
@@@@@@&&BBBB####PPP5PPP5?55?JP5PGP#&&&##BBG@ |==================================================|
@@@@@@@@@&##BG5PPPP55PPPPPY^^?^5&GP5PYG###&@ |= "Building and battling Gunpla is merely a hobby.|
@@@@@@@@@@@@&GPGGPGYYJ5PY5555YY#B5YYY5B@@@@@ |= Unlike the Mobile Suit Gundam story             |
@@@@@@@@@@@@@#PG5JP5JJ5Y?!~JJ7!~!7?JPGB@@@@@ |= we're not in a state of war and we don't have to|
@@@@@@@@@@@@@&GPP5PGP5GPYYYY7!!!!!JP5PGB@@@@ |= put our lives on the line. It's just played     |
@@@@@@@@@@@@@&PPGY5YPGPPYYY5555YYJ5Y55GG&@@@ |= for pleasure. You're absolutely right.          |
@@@@@@@@@@@@@#GGY5YPG?YPYJJJ5G5YJJ55G5YGB@@@ |= But... No                                       |
@@@@@@@@@@@@@BGY5G55J7GPGGPJJGP5YJGPPGBGG&@@ |= for that very reason, people can be enthralled  |
@@@@@@@@@@@@@BGP#GPY?Y555@&G5GBGP5PYYB@##@@@ |= by Gunpla and Gunpla Battle."                   |
@@@@@@@@@@@@@&&@#YYJY5YYG@@&GPGBPPPP5YP&@@@@ |= - Mr. Ral, Gundam Build Fighters episode 6      |
@@@@@@@@@@@@@@@BJJJJYYPB&@@@BGGBGGGGPP5YP#@@ |==================================================|
@@@@@@@@@@@@@&PYYJ55PB&@@@@@@&&&&&&####BGB@@ |==================================================|
@@@@@@@@@@@@@&##B#&@@@@@@@@@@@@@@@@@@@@@@@@@ |==================================================|
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ |==================================================|
                """)
        pilihan = int(input("Pilih menu: "))
        
        if pilihan == 1:
            data_list_gundam(gundam)
        elif pilihan == 2:
            gundam = tambah_gundam(gundam)
        elif pilihan == 3:
            gundam = updaate_gundam(gundam)
        elif pilihan == 4:
            gundam = hapus_gundam(gundam)
        elif pilihan == 5:
            print("kembali ke menu login")
            break
        else:
            print("Pilihan tidak valid.")

# menu pelancong
def pilihan_pelancong(gundam):
    while True:
        print("""
|==================================================|
|=SELAMAT DATANG KOMANDAN,                        =|
|=silahkan pilih menu pelancong dulu              =|
|= 1. tampilkan list koleksi.                     =|
|= 2. keluar dari list koleksi                    =|   
|==================================================|
        """)
        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            data_list_gundam(gundam)
        elif pilihan == 2:
            print("kembali ke menu login")
            break
        else:
            print("Pilihan tidak valid.")

# menu login
def menu_login():
    print("""
|\________________________________________________________/|
|Selamat datang komandan!                                  |
|Coba untuk login atau register, apakah ingin              |
|menambahkan koleksi atau hanya lihat-lihat.               |
|==================== 1. Login      ====================== |
|==================== 2. Register   ====================== |
|==================== 3. Keluar     ====================== |
|__________________________________________________________|
    """)
# Fungsi utama untuk menjalankan program
def main():
    while True:
        menu_login()

        pilihan = int(input("Pilih menu: "))
        if pilihan == 1:
            komandan, role = login(users)
            if komandan:
                if role == "owner":
                    pilihan_owner(gundam)
                else:
                    pilihan_pelancong(gundam)

        elif pilihan == 2:
            register(users)

        elif pilihan == 3:
            print("Terima kasih telah mampir.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

while (True):
    main()
