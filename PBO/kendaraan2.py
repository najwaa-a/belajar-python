# Contoh PBO Pewarisan 
# Memungkinkan kelas anak mewarisi atribut dan metode dari kelas induk 

# kelas Induk: 
class kendaraan2:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
    
    def info(self):
        print(f"Kendaraan: {self.merk}, Tahun: {self.tahun}")

# Kelas anak (Mewarisi dari kendaraan2): 
class Mobil(kendaraan2):
    def __init__(self, merk, tahun, jumlah_pintu):
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        print(f"Mobil: {self.merk}, Tahun: {self.tahun}, jumlah Pintu: {self.jumlah_pintu}")

# Membuat objek dari kelas anak:
mobil1 = Mobil("Honda", 2022, 4)
mobil1.info()  # output ~>  Mobil: Honda, Tahun: 2022, jumlah Pintu: 4        