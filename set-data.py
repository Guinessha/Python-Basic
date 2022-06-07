#python set
#add(), clear(), pop(), union(), issuperset(), issubset(), intersection()
#difference(), isdisjoint(), setdiscard(), copy()

#Himpunan data Set
fruits = {"Melon", "Semangka", "Rambutan", "Paprika", "Apel"}
vegetable = {"Bayam", "tomat", "Paprika", "Brokoli", "Terong"}

#Mengkonversi list kedalam set
trans = set(["Mobil", "Motor", "Bus", "Kereta"])

#Set dengan tipe data yang berbeda-beda
data_campuran = {"Gunung", "Sawah", 5, True, ("A", "B")}

#Fungsi-Fungsi dalam Data Set
#A. FUNGSI MENGHAPUS & MENAMBAH ANGGOTA
#1. add() : Berfungsi menambahkan anggota baru kedalam set
fruits.add("Jeruk")
vegetable.add("Sawi")
trans.add("Becak")
data_campuran.add(17)

#2. clear() : Menghapus semua anggota didalam set
"""fruits.clear()
vegetable.clear()
trans.clear()
data_campuran.add()"""

#3. Remove() : Menghapus nilai yang dicari, Jika nilai yang dicari tidak ada, maka akan error.
fruits.remove("Melon")
vegetable.remove("Bayam")
trans.remove("Mobil")
data_campuran.remove(17)

#4. Discard(): Menghapus nilai yang dicari, Jika nilai yang dicari tidak ada, maka tidak akan error.
"""fruits.remove("alpukat")
vegetable.remove("kangkung")
trans.remove("angkot")
data_campuran.remove(9)"""

#5. pop() : Mengambil dan menghapus nilai yang ada di sebelah kiri
fruits.pop()
vegetable.pop()
trans.pop()
data_campuran.pop()

#6. copy() : Membuat salinan satu set menjadi set baru
salin_buah = fruits.copy()

#FUNGSI KEANGGOTAAN PADA SET
#1. union() : Menggabungkan kedua anggota set
print(fruits.union(trans))
print(vegetable.union(data_campuran))
print(fruits | vegetable) #simbol pipe (|)

#2. Intersection() : fungsi irisan
print(fruits.intersection(vegetable)) #atau menggunakan
print(fruits & vegetable)

#3. Difference() : atau selisih adalah proses mengekstrak anggota grup pertama, yang bukan anggota grup kedua.
print(fruits.difference(vegetable))
print(fruits - vegetable)
print(fruits.symmetric_difference(vegetable)) #symmetric difference akan menghasilkan anggota-anggota dari kedua grup, yang mana tiap anggota tersebut hanya menjadi anggota dari satu grup saja.

#Print himpunan
print(fruits)
print(vegetable)
print(trans)
print(data_campuran)
print(salin_buah)

# Menggunakan perulangan For
for buah in fruits:
    print(buah)
