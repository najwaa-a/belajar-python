#Lambda dalam Python adalah fungsi anonim (tanpa nama) yang digunakan untuk menulis kode singkat dalam satu baris. 

#lambda argumen : ekspresi
    #lambda ~> kata kunci untuk membuat fungsi lambda
    #argumen ~> Parameter yang diteruskan ke fungsi
    #ekspresi ~> Operasi atau perhitungan yang akan dikembalikan

#Fungsi Biasa:
def kuadrat(x): 
    return x ** 2  
print(kuadrat(5)) # output

#Fungsi dengan lambda:
kuadrat_lambda = lambda x: x ** 2
print(kuadrat_lambda(5))  # output

# outputnya akan sama, yaitu 25. 

# Lambda dengan 2 parameter
tambah = lambda a, b: a + b
print(tambah(3, 7)) # outputnya 10