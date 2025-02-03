# a) List (list) ~> Kumpulan data yang bisa berubal (mutable)
buah = ["Apel", "Jeruk", "Mangga"]
buah.append("Pisang")
print(buah[1]) # Outputnya adalah Jeruk
print(buah)  # Outputnya adalah ['Apel', 'Jeruk', 'Mangga', 'Pisang']

# b) Tuple (tuple) ~> Kumpulan data yang tidak bisa diubah (immmutable)
warna = ("Merah", "Hijau", "Biru")
print(warna[1]) # Outputnya adalah Hijau, angka 1 menunjukan urutan variabel 

# c) Dictionary(dict) ~> Kumpulan data dalam pasangan key-value
mahasiswa = {"nama": "Budi", "umur": 21, "jurusan": "Informatika"}
print(mahasiswa["nama"]) # Outputnya adalah Budi
mahasiswa["umur"] = 22 # Mengubah nilai
print(mahasiswa) # Outputnya adalah {'nama': 'Budi', 'umur': 22, 'jurusan': 'Informatika'}  

# d) Set (set) ~> Kumpulan data unik (tidak ada duplikasi)
angka = {1, 2, 3, 3, 4, 4}
print(angka) # Outputnya adalah {1, 2, 3, 4} (Otomatis menghapus duplikatnya)
