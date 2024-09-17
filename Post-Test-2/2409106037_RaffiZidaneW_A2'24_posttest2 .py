nama = input("masukan nama untuk membeli beras:")
nim = input("sekalian nim dong ganteng:")
harga = int(input("harga berapa?:"))
diskonMawar = harga * 0.11
hargamawar = harga - diskonMawar
diskonSania = harga * 0.14
hargaSania = harga - diskonSania
diskonMaknyus = harga * 0.17
hargaMaknyus = harga - diskonMaknyus
print(f"""{nama} dengan Nim {nim} ingin membeli beras seharga Rp {harga}
      Jika dia membeli beras Mawar ia harus membayar Rp {hargamawar:} setelah mendapat diskon 11%.
      Jika dia membeli beras Sania ia harus membayar Rp {hargaSania:} setelah mendapat diskon 14%.
      Jika dia membeli beras Maknyus ia harus membayar Rp {hargaMaknyus:} setelah mendapat diskon 17%.""")

