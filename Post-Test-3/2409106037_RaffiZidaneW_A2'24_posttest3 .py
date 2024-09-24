nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
pinjaman = int(input("Masukkan jumlah pinjaman (Rp): "))
lamapinjaman = int(input("Masukkan lama pinjaman (tahun): "))

if lamapinjaman == 1:
    bungatahunan = 0.07
elif lamapinjaman == 2:
    bungatahunan = 0.13
elif lamapinjaman == 3:
    bungatahunan = 0.19
else:
    print("Lama cicilan tidak valid")

bungabulanan = (bungatahunan / 12) * pinjaman
jumlahbulan = 12 * lamapinjaman
totalcicilan = (pinjaman + bungabulanan) / jumlahbulan

print(f"""Nama: {nama}
      nim: {nim}
      total cicilan yang dibayar perbulan: rp {totalcicilan}""")