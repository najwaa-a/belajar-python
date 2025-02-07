for index in range(3, 8): # digunakan untuk mengakses elemen array
    x = index * 10 # 30, 40, 50, 60, 70, 80
    if index == 5: # skip 50
        continue # fungsinya untuk melompati iterasi saat index = 5
    print(x) # prints: 30, 40, 50, 60, 70