# menggunakan default parameter sbg pengganti metode overloading

class kalkulator:
    def tambah(self, a, b, c=0):
        return a + b + c
    
k = kalkulator()
print(k.tambah(2, 3))
print(k.tambah(2, 3, 4))