#python Dictionary

#Cara Membuat Dictionary
#1). Dengan tanda {}
topik_belajar = {
    "Judul" : "Belajar python list, set, tuple dan dictionary",
    "Waktu" : "Jam 9 pagi sampai jam 12 siang",
    "Alat" : "Laptop saja"
}

#2). Dengan dict()
belajar_python = dict(
    Judul = "Belajar python list, set, tuple dan dictionary",
    Waktu = "Jam 9 pagi sampai jam 12 siang",
    Alat = "Laptop saja"
)

#Cara Mengakses Item Pada Dictionary
#1) Dengan menggunakan kurung siku ([])
print("Judul hari ini adalah: ", topik_belajar["Judul"])

#2) Dengan menggunakan fungsi get()
print("Judul hari ini adalah:", belajar_python.get('Judul'))

#Perulangan Untuk Dictionary
for key in topik_belajar:
    print(key, '->', topik_belajar[key])
    
#Mengubah Nilai Item
print("Judul awal:", topik_belajar.get('Judul'))
topik_belajar['Judul'] = "Sudah Selesai"
print("Judul setelah diubah:", topik_belajar.get('Judul'))

#Menambahkan Item
biodata = {
    "Nama" : "Tico Guinessha S",
    "Asal" : "Indonesia"
}

print("Hobi", biodata.get('Hobi'))
biodata["Hobi"] = "Programming"
print("Hobi dari {} adalah {}".format(
    biodata.get("Nama"),
    biodata.get('Hobi')
))

#Menghapus Item
capital = {
    "Amerika" : "New York",
    "Indonesia" : "Jakarta",
    "Spanyol" : "Madrid",
    "Jepang" : "Tokyo",
    "Malaysia" : "Kuala Lumpur"
}
#1) Menggunakan statement del <dict[key]>.
del capital['Malaysia']
print(capital)
#2) Menggunakan fungsi dictionary.pop() : kalau menggunakan fungsi pop(), kita bisa mendapatkan nilai kembalian dari data yang telah dihapus.
capital.pop('Amerika')
print(capital)

#Operator Keanggotaan
biodata = {
    "Nama" : "Tico Guinessha S",
    "Asal" : "Indonesia",
    "Usia" : 21
}

print("Apakah variabel biodata memiliki key nama?")
print("Nama" in biodata)

print("\nApakah variabel biodata tidak memiliki key usia?")
print('Usia' not in biodata)

#Panjang atau Banyak Key Pada Dictionary
print("Panjang atau banyak key pada dictionary:", (len(biodata)))

