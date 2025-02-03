# menggunakan lambda function
kuadrat = lambda x: x ** 2
print(kuadrat(5))

# menggunakan map dan filter
angka = [1, 2, 3, 4, 5]
hasil = list(map(lambda x: x * 2, angka)) # Mengalikan semua angka dengan 2
print(hasil)