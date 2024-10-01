# bang ini saya pakai python yang langsung dari flowgorithm,bisa dikurangi langsung nilai saya jika tidak sesuai kriteria penilaian abang
percobaan = 0
while percobaan <= 3:
    print("silahkan login")
    print("masukkan nama:")
    nama = input()
    print("nim nya juga, cukup 3 angka belakang")
    print("nim sebagai password")
    nim = int(input())
    if nama == "raffi zw" and nim == 37:
        print("met datang di blunbank,hanya melayani pinjaman uang")
        print("berapa yang ingin di pinjam")
        pinjaman = int(input())
        print("seberapa lama pinjaman?")
        print("1 untuk 1 tahun, 2 untuk 2 tahun, dan 3 untuk 3 tahun")
        lamapinjaman = int(input())
        jumlahbulan = 12 * lamapinjaman
        if lamapinjaman == 1:
            bungatahunan = 0.07
            bungabulanan = bungatahunan / 12 * pinjaman
            totalcicilan = (pinjaman + bungabulanan) / jumlahbulan
            print(f"{nama} dengan NIM {nim}, total cicilan yang dibayar per bulan: {totalcicilan}, dibayar 1 tahun.")
        else:
            if lamapinjaman == 2:
                bungatahunan = 0.13
                bungabulanan = bungatahunan / 12 * pinjaman
                totalcicilan = (pinjaman + bungabulanan) / jumlahbulan
                print(f"{nama} dengan NIM {nim}, total cicilan yang dibayar per bulan: {totalcicilan}, dibayar 2 tahun.")
            else:
                if lamapinjaman == 3:
                    bungatahunan = 0.19
                    bungabulanan = bungatahunan / 12 * pinjaman
                    totalcicilan = (pinjaman + bungabulanan) / jumlahbulan
                    print(f"{nama} dengan NIM {nim}, total cicilan yang dibayar per bulan: {totalcicilan}, dibayar 3 tahun.")
                else:
                    print("tidak masuk s.o.p bank")
        print("yakin dengan total pinjaman dan lama pinjamannya nya?jika tidak ketik t jika sudah yakin pencet y")
        ulang = input()
        if ulang == "y":
            print("bayar sesuai waktu")
            break
        else:
            print("silahkan diulang lagi dari login ya")
    else:
        percobaan = percobaan + 1
        print("ulang dong,masukkan nama dan nim yang benar sesuai ketentuan")
if percobaan == 3:
    print("karna salah 3 kali maka akun ada di blokir,silahkan ke bank terdekat untuk memulihkannya")