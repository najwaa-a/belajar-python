nums = [60, 70, 30, 110, 90]
for n in nums:
    if n >= 100: # digunakan untuk memeriksa apakah nilai n lebih besar atau sama dengan 100
        print("%d is bigger than 100" %n) # digunakan untuk mencetak string dan integer secara bersamaan
        break # digunakan untuk menghentikan loop
else:
    print("Not Found!") # digunakan untuk mencetak string jika tidak ada nilai yang memenuhi kondisi if