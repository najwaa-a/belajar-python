# Contoh PBO Polimorfisme dalam Python

class ratna:
    def bakat(self):
        print("ratna pintar Bernyanyi")

class riski:
    def bakat(self):
        print("riski pintar Menari")

murid1 = ratna()
murid2 = riski()

for murid in (murid1, murid2):
    murid.bakat()