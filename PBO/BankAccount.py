# Contoh Enkapsulasi PBO pada Python
#  metode menyembunyikan data dengan membuat atribut bersifat private menggunakan tanda __ (double underscore) 

class BankAccount:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo # atribut private

    def lihat_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.__saldo}")
    
    def deposit(self, jumlah):
        self.__saldo += jumlah
        print(f"Deposit Rp{jumlah}. Saldo baru: Rp{self.__saldo}") 
    
    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup!")
        else:
            self.__saldo -= jumlah
            print(f"Penarikan Rp{jumlah}. Saldo tersisa: Rp{self.__saldo}")


# Membuat objek
akun1 = BankAccount("Budi", 1000000)
akun1.lihat_saldo()
akun1.deposit(500000)
akun1.tarik(200000)
