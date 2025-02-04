# Contoh PBO Polimorfisme dalam Python
# Memungkinkan metode dengan nama yang sama tetapi memiliki perilaku yang berbeda

class Burung:
    def bersuara(self):
        print("Burung berkicau")


class Anjing:
    def bersuara(self):
        print("Anjing menggonggong")


# Polimorfisme dalam aksi : 
hewan1 = Burung()
hewan2 = Anjing()

for hewan in (hewan1, hewan2):
    hewan.bersuara()