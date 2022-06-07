#python Tuple

#Bagaimana cara membuat tuple?
tuple_kosong = ()
#1. Cara Standart
nilai = ("Siang", "Malam", "Sore", "Pagi")
#2. Menggunakan fungsi tuple dan melemparkan list sebagai parameternya
nilai = tuple(["Siang", "Malam", "Sore", "Pagi"])

#3. Tuple yang berisikan 1 item
nomor = (10)
angka = (10,) #kita tetap diharuskan menulis tanda koma.
print(type(10)) #Interger biasa
print(type((10,))) #Tuple

#Cara mengakses nilai tuple
country =("Amerika", "Spanyol", "Jepang", "Swiss")

print(country[2]) #indeks 2
print(country[3]) #indeks 4
print(country[-3]) 

#Slicing tuple
fruits = ("Melon", "Semangka", "Rambutan", "Paprika", "Apel", "Duku", "Nanas")

#1) Slicing dengan batas
print(fruits[2:3])
print(fruits[0:2])
print(fruits[1:2])

#2) Slicing tanpa batas
print(fruits[:2])
print(fruits[0:])
print(fruits[:4])

#Sequence Unpacking
biodata = ("Tico", "Indonesia", 21)

Nama, Asal, Umur = biodata
print("Nama:", Nama)
print("Umur:", Umur)
print("Asal:", Asal)


#Menggabungkan dua buah tuple atau lebih
x = (1, 2, 3, 4, 5)
y = (6, 7, 8, 9, 10)
z = x + y
print(z)

#Fungsi-fungsi bawaan tuple
country_2 =("Amerika", "Spanyol", "Jepang", "Swiss", "Indonesia", "Italia")

print(len(country_2))
print(max(z))
print(min(z))          