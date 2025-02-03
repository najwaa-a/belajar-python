# a. Lambda dengan menggunakan map() untuk transformasi data
angka = [1, 2, 3, 4, 5]
hasil = list(map(lambda x: x * 2, angka)) # semua angka dikalikan 2
print(hasil) # outputnya [2, 4, 6, 8, 10]

# b. Lambda dengan menggunakan filter() untuk menyaring data
angka = [1, 2, 3, 4, 5, 6]
genap = list(filter(lambda x: x % 2 == 0, angka)) # Mengambil angka genap
print(genap) # outputnya [2, 4, 6]

# c. Lambda dengan menggunakan sorted() untuk sorting dengan lambda
data = [("Budi", 25), ("Ani", 19), ("Citra", 22)]
    #Sorting berdasarkan umur (indeks ke-1 dalam tuple ~> urutan nilai yang terurut dan tidak dapat diubah) 
data_sorted = sorted(data, key=lambda x: x[1])
print(data_sorted) # outputnya [('Ani', 19), ('Citra', 22), ('Budi', 25)]