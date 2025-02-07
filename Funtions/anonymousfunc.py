a = (lambda x: x > 2)(3) # Fungsi lambda yang menerima satu parameter x dan mengembalikan true jika x > 2 atau false jika tidak
print(a) # memanggil fungsi x = 3 || 3 > 2 maka a = true

b = (lambda x, y: x ** 2 + y ** 2)(2, 1) # Fungsi lambda dengan 2 parameter (x dan y), yang menghitung: x^2 + y^2
print(b)  # memanggl fungsi x = 2 || y = 1 || 2^2 + 1^2 = 4 + 1 = 5, maka b = 5