def swap(x, y): # digunakan untuk mengembalikan y, x
    return y, x # mengembalikan tuple (y, x)

x = 1
y = 2
x, y = swap(x, y) # mengembalikan (2, 1), maka hasilnya x dan y ditukar x = 2, y = 1
print(x, y) # ouutputnya 2 1