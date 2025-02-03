class Mahasiswa:
    def __init__(self, nama, nim): # beri spasi antara def dan __init__
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        print(f"Hallo, saya {self.nama}, NIM saya {self.nim}")

mhs1 = Mahasiswa("Budi", "10312240028")
mhs1.perkenalan()