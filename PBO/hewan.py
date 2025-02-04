# Contoh PBO Abstraksi dalam Python
# Membuat kerangka dasar kelas tanpa harus mengimplementasikannya langsung

from abc import ABC, abstractmethod # import ABC dan abstractmethod dari modul abc

# Kelas abstrak:
class Hewan(ABC):
    @abstractmethod  
    def bersuara(self):
        pass

# Kelas turunannya:
class Kucing(Hewan):
    def bersuara(self):
        print("Meeeeow!")

class Sapi(Hewan):
    def bersuara(self):
        print("Mooooo!")


# Membuat objek
kucing = Kucing()
sapi = Sapi()

kucing.bersuara()
sapi.bersuara()
