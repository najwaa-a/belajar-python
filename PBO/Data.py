class Data:
    __info = "Data Rahasia" # private attribute

    def get_info(self):
        return self.__info # Menggunakan method untuk akses
    
d = Data()
print(d.get_info()) # Bisa diakses melalui method