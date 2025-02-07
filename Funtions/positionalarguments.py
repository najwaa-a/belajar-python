def varargs(*args): # *args adalah parameter variabel yang digunakan untuk menerima argumen yang tidak terduga
    return args # return nilai dari parameter variabel
print(varargs(1, 2, 3, 4, 5))  # Output: (1, 2, 3, 4, 5)