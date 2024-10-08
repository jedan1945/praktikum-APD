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
users = [["raffi", "37", "owner"]]
gundam = [["freedom", "hg", "dirakit" ],
        ["00 shia qant", "hg", "dirakit" ],
        ["dynames huang zhong", "sd", "dirakit"],
        ["gundam x", "mg" , "mib"]] #mib mint in box,belum dirakit

while True:
    pilihan = int(input("Pilih menu login: "))

    if pilihan == 1:
        komandan = input("komandan: ")
        password = input("Password: ")
        user = None
        
        for i in users:
            if i[0] == komandan and i[1] == password:
                user = i
                break
        
        if user is None:
            print("Login gagal komandan, nama komandan atau password salah.")
        else:
            print(f"Selamat datang, komandan {komandan}!")
            while True:
                if user[2] == "owner":
                    print("""
@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@ |==================================================|
@@@@@@@@@@@@@@@@@@@@@BPB&@@@@@@@@@@@#5#@@@@@ |==================================================|
@@@@@@@@@@@@&&@@@@@@@@PJ7?#@@@@@@@&G75@@@@@@ |==================================================|
@@@@@@@@@@@@@BPB&@@@@@@PJ~P&&###&@@YJ@@@#B&@ |=SELAMAT DATANG KOMANDAN,silahkan pilih menu dulu=|
@@@@@@@@@@@@@@&PJJP#&BGG5?!GGGPPP##J#@#YY&@@ |= 1.tampilkan data list koleksi.                  |
@@@@@@@@@@@@@@@@GJ7!!?JY55?JBGGG5P5P#5!5@@@@ |= 2.tambah data list koleksi.                     |
@@@@@@@@@@@@@@@&G5PYJ?7!!!77JPB55Y7!!7G@@@@@ |= 3.update data koleksi.                          |
@@@@@@@@@@@@@@@&G5PPPPPP5YJ?75P55JYB&&@@@@@@ |= 4.hapus data koleksi.                           |
@@@@@@@@@@@@@@@&GPPPPPB5?#75PB5Y5B@@@@@@@@@@ |= 5.keluar dari data koleksi.                     |
@@@@@@&&BBBB####PPP5PPP5?55?JP5PGP#&&&##BBG@ |==================================================|
@@@@@@@@@&##BG5PPPP55PPPPPY^^?^5&GP5PYG###&@ |= "Building and battling Gunpla is merely a hobby.|
@@@@@@@@@@@@&GPGGPGYYJ5PY5555YY#B5YYY5B@@@@@ |= Unlike the Mobile Suit Gundam story             |
@@@@@@@@@@@@@#PG5JP5JJ5Y?!~JJ7!~!7?JPGB@@@@@ |= we're not in a state of war and we don't have to|
@@@@@@@@@@@@@&GPP5PGP5GPYYYY7!!!!!JP5PGB@@@@ |= put our lives on the line It's just played      |
@@@@@@@@@@@@@&PPGY5YPGPPYYY5555YYJ5Y55GG&@@@ |= for pleasure You're absolutely right.           |
@@@@@@@@@@@@@#GGY5YPG?YPYJJJ5G5YJJ55G5YGB@@@ |= But... No                                       |
@@@@@@@@@@@@@BGY5G55J7GPGGPJJGP5YJGPPGBGG&@@ |= for that very reason people can be enthralled   |
@@@@@@@@@@@@@BGP#GPY?Y555@&G5GBGP5PYYB@##@@@ |= by Gunpla and Gunpla Battle."                   |
@@@@@@@@@@@@@&&@#YYJY5YYG@@&GPGBPPPP5YP&@@@@ |= -Mr.Ral Gundam Build Fighters episode 6         |
@@@@@@@@@@@@@@@BJJJJYYPB&@@@BGGBGGGGPP5YP#@@ |==================================================|                                                  
@@@@@@@@@@@@@&PYYJ55PB&@@@@@@&&&&&&####BGB@@ |==================================================|
@@@@@@@@@@@@@&##B#&@@@@@@@@@@@@@@@@@@@@@@@@@ |==================================================|
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ |==================================================|
                        """)
                    pilihan_owner = int(input("Pilih menu: "))

                    if pilihan_owner == 1:
                        if len(gundam) == 0:
                            print("belum koleksi gundam")
                        else:
                            for i, item in enumerate(gundam):
                                print(f"{i + 1}. {item[0]} - grade: {item[1]} - kondisi: {item[2]}")

                    elif pilihan_owner == 2:
                        # Tambah Menu
                        nama = input("Masukkan nama gundam: ")
                        grade = input("Masukkan grade: ")
                        kondisi = input("Masukkan kondisi: ")

                        # Validasi input angka secara manual
                        if (grade) and (kondisi):
                            gundam.append([nama, grade, kondisi])
                            print(f"gundam {nama} berhasil ditambahkan dalam koleksi.")
                        else:
                            print("Input harga dan stok harus berupa angka.")

                    elif pilihan_owner == 3:
                        # Update Menu
                        if len(gundam) == 0:
                            print("belum koleksi gundam.")
                        else:
                            for i, item in enumerate(gundam):
                                print(f"{i + 1}. {item[0]} - Harga: {item[1]} - Stok: {item[2]}")

                            index = input("Masukkan nomor gundam yang ingin diupdate: ")

                            if (index) and 0 < int(index) <= len(gundam):
                                index = int(index) - 1
                                nama_baru = input("Masukkan nama gundam baru (kosongkan jika tidak ingin mengubah): ")
                                grade_baru = input("Masukkan grade gundambaru (kosongkan jika tidak ingin mengubah): ")
                                kondisi_baru = input("Masukkan kondisi gundam baru (kosongkan jika tidak ingin mengubah): ")

                                if nama_baru:
                                    gundam[index][0] = nama_baru
                                if (grade_baru):
                                    gundam[index][1] = grade_baru
                                if (kondisi_baru):
                                    gundam[index][2] = kondisi_baru

                                print("gundam berhasil diupdate.")
                            else:
                                print("Nomor gundam tidak valid.")

                    elif pilihan_owner == 4:
                        # Hapus Menu
                        if len(gundam) == 0:
                            print("belum koleksi gundam.")
                        else:
                            for i, item in enumerate(gundam):
                                print(f"{i + 1}. {item[0]} - grade: {item[1]} - kondisi: {item[2]}")

                            index = input("Masukkan nomor gundam yang ingin dihapus: ")

                            if(index) and 0 < int(index) <= len(gundam):
                                index = int(index) - 1
                                del gundam[index]
                                print("gundam berhasil dihapus.")
                            else:
                                print("Nomor gundam tidak valid.")

                    elif pilihan_owner == 5:
                        break

                    else:
                        print("Pilihan tidak valid.")

                else:
                    # Menu untuk pelancong
                    print("""\n
|==================================================|
|=SELAMAT DATANG KOMANDAN,                        =|
|=silahkan pilih menu pelancong dulu              =|
|= 1.tampilkan list koleksi.                      =|
|= 2.keluar dari list koleksi                     =|   
|=#untuk menu lainnya masi dalam pengembangan     =|
|==================================================|
                          """)
                    pilihan_pelancong = int(input("Pilih menu: "))
                    # tampilkan
                    if pilihan_pelancong == 1:
                        if len(gundam) == 0:
                            print("belum koleksi gundam.")
                        else:
                            for i, item in enumerate(gundam):
                                print(f"{i + 1}. {item[0]} - grade: {item[1]} - kondisi: {item[2]}")

                    elif pilihan_pelancong == 2:
                        break

                    else:
                        print("Pilihan tidak valid.")
    if pilihan == 2:
        # Register
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        role = input("Masukkan role (admin/pelancong): ")
        
        if role == "admin" or role == "pelancong":
            users.append([username, password, role])
            print(f"Pengguna {username} berhasil didaftarkan.")
        else:
            print("Role tidak valid. Harus admin atau pelancong.")
            break

    if pilihan == 3:
        print("Terima kasih telah sudah mampir ke tempat ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")




print("""
@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@BPB&@@@@@@@@@@@#5#@@@@@
@@@@@@@@@@@@&&@@@@@@@@PJ7?#@@@@@@@&G75@@@@@@
@@@@@@@@@@@@@BPB&@@@@@@PJ~P&&###&@@YJ@@@#B&@
@@@@@@@@@@@@@@&PJJP#&BGG5?!GGGPPP##J#@#YY&@@
@@@@@@@@@@@@@@@@GJ7!!?JY55?JBGGG5P5P#5!5@@@@
@@@@@@@@@@@@@@@&G5PYJ?7!!!77JPB55Y7!!7G@@@@@
@@@@@@@@@@@@@@@&G5PPPPPP5YJ?75P55JYB&&@@@@@@
@@@@@@@@@@@@@@@&GPPPPPB5?#75PB5Y5B@@@@@@@@@@
@@@@@@&&BBBB####PPP5PPP5?55?JP5PGP#&&&##BBG@
@@@@@@@@@&##BG5PPPP55PPPPPY^^?^5&GP5PYG###&@
@@@@@@@@@@@@&GPGGPGYYJ5PY5555YY#B5YYY5B@@@@@ 
@@@@@@@@@@@@@#PG5JP5JJ5Y?!~JJ7!~!7?JPGB@@@@@ 
@@@@@@@@@@@@@&GPP5PGP5GPYYYY7!!!!!JP5PGB@@@@ 
@@@@@@@@@@@@@&PPGY5YPGPPYYY5555YYJ5Y55GG&@@@ 
@@@@@@@@@@@@@#GGY5YPG?YPYJJJ5G5YJJ55G5YGB@@@
@@@@@@@@@@@@@BGY5G55J7GPGGPJJGP5YJGPPGBGG&@@
@@@@@@@@@@@@@BGP#GPY?Y555@&G5GBGP5PYYB@##@@@ 
@@@@@@@@@@@@@&&@#YYJY5YYG@@&GPGBPPPP5YP&@@@@ 
@@@@@@@@@@@@@@@BJJJJYYPB&@@@BGGBGGGGPP5YP#@@                                                
@@@@@@@@@@@@@&PYYJ55PB&@@@@@@&&&&&&####BGB@@ 
@@@@@@@@@@@@@&##B#&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@"i'm gundam" setsuna f seiei.@@@@@@@@
@terimah kasi telah datang ke data koleksi.@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
""")