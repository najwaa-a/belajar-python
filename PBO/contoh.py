#Destructor otomatis dipanggil ketika objek dihapus dari memori

class Contoh:
    def __del__(self): # sebagai destructor
        print("Object dihancurkan")

obj = Contoh()
del obj # memanggil destructor