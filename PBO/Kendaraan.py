# Contoh PBO Dasar dalam python

# Membuat kelas (Class):
class Kendaraan:
    def __init__(self, merk, tahun): # konsekutor
        self.merk = merk # atribut
        self.tahun = tahun # atribut
    
    def info(self): # method
        print(f"Kendaraan: {self.merk}, Tahun: {self.tahun}") 

# Membuat objek dari kelas kendaraan : 
Kendaraan1 = Kendaraan("Toyota", 2020)
Kendaraan1.info()