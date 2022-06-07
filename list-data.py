#python List

#HIMPUNAN DATA LIST
animals = ["Singa", "Gajah", "Harimau", "Hiu"]
home = ["Sofa", "Dapur", "Meja", "Komputer"]

#List kumpulan interger
angka =[17, 9, 2001]

#List data campuran
data_campuran =["Buaya", 20, False, 13.3]

#Fungsi-Fungsi dalam Data List
#1. Menampilkan isi tertentu dari list dengan menggunakan indeks
print(animals[2])
print(home[1])
print(angka[0])
print(data_campuran[3])

#2. Slicing data
print("2. Slicing Data List")
print(animals[0:2])
print(home[:2])
print(angka[0:])
print(data_campuran[:1])

#3. Mengubah data di dalam list
print("3. Mengubah data di dalam list")
animals[1] = "Jerapah"
print(animals)
home[0:1] = ["Ruang makan", "TV"]
print(home)
angka[2] = 21
print(angka)
data_campuran[2] = 12.2
print(data_campuran)

#A. FUNGSI MENGHAPUS & MENAMBAH ANGGOTA
#4. append() : Menambah item ke dalam list dibelakang
print("4. append()")
animals.append("Buaya")
print(animals)
home.append("Lantai")
print(home)
angka.append("100")
print(angka)
data_campuran.append("Samsul")
print(data_campuran)

#5. insert() : Menambah item ke dalam list di depan/dimanapun
print("5. insert()")
animals.insert(0, "Burung")
print(animals)
home.insert(2, "Atap")
print(home)

#6. pop() : akan mengambil item terakhir dari sebuah list, lalu menghapusnya
print("6. pop()")
terhapus = animals.pop()
print("File yang Terhapus:", terhapus)
print(animals)

#7. remove() : Fungsi ini akan menghapus data yang memiliki nilai yang sama dengan parameter yang dimasukkan.
print("7. remove()")
animals.remove("Jerapah")
print(animals)

#8. del : kita bisa menghapus indeks berapa pun dari item list.
print("8. del")
del home[0:2]
print(home)
del angka [3]
print(angka)

#9. Menggabungkan dua buah list atau lebih
print("9. Menggabungkan dua buah list")
animals_2 = ["kuda nil", "kucing"]
print(animals + animals_2)

#10. <list>.sort() : Mengurutkan data | reverse() : membalikkan posisi item list (tidak harus berurut)
print("10. sort() & reverse()")
animals.sort()
print(animals)
angka.sort()
print(angka)
home.reverse()# membalikkan posisi item list (tidak harus berurut)
print(home)
print('\n')

#PRINT HIMPUNAN DATA
print(animals)
print(home)
print(angka)
