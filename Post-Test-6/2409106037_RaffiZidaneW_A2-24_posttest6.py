print("""
       \n
      |\_________________________________________________________/|
      |selamat datang komandan apakah ingin melihat koleksi jidan?|
      |coba untuk login atau register apakah komandan ingin       |
      |menambahkan koleksi atau hanya liat liat                   |
      |======================= 1. login    =======================|
      |======================= 2. register =======================|
      |======================= 3. keluar   =======================|
      |___________________________________________________________|
      """)

users = {
    "raffi": {"password": "37", "role": "owner"}
}

gundam = {
    "freedom": {"grade": "hg", "kondisi": "dirakit"},
    "00 shia qant": {"grade": "hg", "kondisi": "dirakit"},
    "dynames huang zhong": {"grade": "sd", "kondisi": "dirakit"},
    "gundam x": {"grade": "mg", "kondisi": "mib"}  # mib = mint in box, belum dirakit
}

while True:
    pilihan = int(input("Pilih menu login: "))

    if pilihan == 1:
        komandan = input("Komandan: ")
        password = input("Password: ")

        if komandan in users and users[komandan]["password"] == password:
            print(f"Selamat datang, komandan {komandan}!")
            role = users[komandan]["role"]
            while True:
                if role == "owner":
                    print("""
@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@ |==================================================|
@@@@@@@@@@@@@@@@@@@@@BPB&@@@@@@@@@@@#5#@@@@@ |==================================================|
@@@@@@@@@@@@&&@@@@@@@@PJ7?#@@@@@@@&G75@@@@@@ |==================================================|
@@@@@@@@@@@@@BPB&@@@@@@PJ~P&&###&@@YJ@@@#B&@ |=SELAMAT DATANG KOMANDAN, silahkan pilih menu dulu=|
@@@@@@@@@@@@@@&PJJP#&BGG5?!GGGPPP##J#@#YY&@@ |= 1. tampilkan data list koleksi.                  |
@@@@@@@@@@@@@@@@GJ7!!?JY55?JBGGG5P5P#5!5@@@@ |= 2. tambah data list koleksi.                     |
@@@@@@@@@@@@@@@&G5PYJ?7!!!77JPB55Y7!!7G@@@@@ |= 3. update data koleksi.                          |
@@@@@@@@@@@@@@@&G5PPPPPP5YJ?75P55JYB&&@@@@@@ |= 4. hapus data koleksi.                           |
@@@@@@@@@@@@@@@&G5PPPB5?#75PB5Y5B@@@@@@@@@@@ |= 5. keluar dari data koleksi.                     |
@@@@@@&&BBBB####PPP5PPP5?55?JP5PGP#&&&##BBG@ |==================================================|
@@@@@@@@@&##BG5PPPP55PPPPPY^^?^5&GP5PYG###&@ |= "Building and battling Gunpla is merely a hobby. |
@@@@@@@@@@@@&GPGGPGYYJ5PY5555YY#B5YYY5B@@@@@ |= Unlike the Mobile Suit Gundam story              |
@@@@@@@@@@@@@#PG5JP5JJ5Y?!~JJ7!~!7?JPGB@@@@@ |= we're not in a state of war and we don't have to |
@@@@@@@@@@@@@&GPP5PGP5GPYYYY7!!!!!JP5PGB@@@@ |= put our lives on the line. It's just played      |
@@@@@@@@@@@@@&PPGY5YPGPPYYY5555YYJ5Y55GG&@@@ |= for pleasure. You're absolutely right.           |
@@@@@@@@@@@@@#GGY5YPG?YPYJJJ5G5YJJ55G5YGB@@@ |= But... No                                       |
@@@@@@@@@@@@@BGY5G55J7GPGGPJJGP5YJGPPGBGG&@@ |= for that very reason, people can be enthralled   |
@@@@@@@@@@@@@BGP#GPY?Y555@&G5GBGP5PYYB@##@@@ |= by Gunpla and Gunpla Battle."                   |
@@@@@@@@@@@@@&&@#YYJY5YYG@@&GPGBPPPP5YP&@@@@ |= - Mr. Ral, Gundam Build Fighters episode 6       |
@@@@@@@@@@@@@@@BJJJJYYPB&@@@BGGBGGGGPP5YP#@@ |==================================================|                                                  
@@@@@@@@@@@@@&PYYJ55PB&@@@@@@&&&&&&####BGB@@ |==================================================|
@@@@@@@@@@@@@&##B#&@@@@@@@@@@@@@@@@@@@@@@@@@ |==================================================|
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ |==================================================|
                        """)
                    pilihan_owner = int(input("Pilih menu: "))
                    if pilihan_owner == 1:
                        if len(gundam) == 0:
                            print("Belum ada koleksi gundam.")
                        else:
                            for i, (nama, info) in enumerate(gundam.items()):
                                print(f"{i + 1}. {nama} - grade: {info['grade']} - kondisi: {info['kondisi']}")

                    elif pilihan_owner == 2:
                        # Tambah Menu
                        nama = input("Masukkan nama gundam: ")
                        grade = input("Masukkan grade: ")
                        kondisi = input("Masukkan kondisi: ")

                        gundam[nama] = {"grade": grade, "kondisi": kondisi}
                        print(f"Gundam {nama} berhasil ditambahkan ke koleksi.")

                    elif pilihan_owner == 3:
                        # Update Menu
                        if len(gundam) == 0:
                            print("Belum ada koleksi gundam.")
                        else:
                            for i, (nama, info) in enumerate(gundam.items()):
                                print(f"{i + 1}. {nama} - grade: {info['grade']} - kondisi: {info['kondisi']}")

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

                    elif pilihan_owner == 4:
                        # Hapus Menu
                        if len(gundam) == 0:
                            print("Belum ada koleksi gundam.")
                        else:
                            for i, (nama, info) in enumerate(gundam.items()):
                                print(f"{i + 1}. {nama} - grade: {info['grade']} - kondisi: {info['kondisi']}")

                            index = int(input("Masukkan nomor gundam yang ingin dihapus: ")) - 1
                            nama_gundam = list(gundam.keys())[index]

                            del gundam[nama_gundam]
                            print(f"Gundam {nama_gundam} berhasil dihapus.")

                    elif pilihan_owner == 5:
                        break

                    else:
                        print("Pilihan tidak valid.")

                else:
                    # Menu untuk pelancong
                    print("""
|==================================================|
|=SELAMAT DATANG KOMANDAN,                        =|
|=silahkan pilih menu pelancong dulu              =|
|= 1. tampilkan list koleksi.                     =|
|= 2. keluar dari list koleksi                    =|   
|==================================================|
                          """)
                    pilihan_pelancong = int(input("Pilih menu: "))

                    if pilihan_pelancong == 1:
                        if len(gundam) == 0:
                            print("Belum ada koleksi gundam.")
                        else:
                            for i, (nama, info) in enumerate(gundam.items()):
                                print(f"{i + 1}. {nama} - grade: {info['grade']} - kondisi: {info['kondisi']}")

                    elif pilihan_pelancong == 2:
                        break

                    else:
                        print("Pilihan tidak valid.")

    elif pilihan == 2:
        # Register
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        role = input("Masukkan role (owner/pelancong): ")

        if role in ["owner", "pelancong"]:
            users[username] = {"password": password, "role": role}
            print(f"Pengguna {username} berhasil didaftarkan.")
        else:
            print("Role tidak valid. Harus owner atau pelancong.")

    elif pilihan == 3:
        print("Terima kasih telah mampir ke tempat ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
