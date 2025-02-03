from collections import deque  # import modul deque

q = deque() # deque kosong
q = deque([1, 2, 3]) # data deque awal

q.append(4) # menambahkan elemen 4 di akhir ~> [1, 2, 3, 4]
q.appendleft(0) # menambahkan elemen 0 di awal ~> [0, 1, 2, 3, 4]
print(q) # outputnya ~> deque([0, 1, 2, 3, 4])

x = q.pop() # menghapus elemen di akhir dan mengembalikan nilai ~> 4
y = q.popleft() # menghapus elemen di awal dan mengembalikan nilai ~> 0
print(x) # outputnya ~> 4
print(y) # outputnya ~> 0
print(q) # outputnya ~> deque ([1, 2, 3])

q.rotate(1) # Rotasi ke kanan 1 langkah
print(q) # outputnya ~> deque ([3, 1, 2])

# deque adalah struktur data seperti list tapi lebih efisien untuk menambah dan menghapus elemen di depan maupun dibelakang.