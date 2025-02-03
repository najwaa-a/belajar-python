from collections import deque

queue = deque()

queue.append("A") # menambah elemen antrian 
queue.append("B")
queue.append("C")

print("Antrian sebelum diproses:", queue)

queue.popleft() # menghapus elemen antrian dari depan
print("Antrian setelah 1 diproses:", queue)

# FIFO (First in, First out) adalah elemen pertama yang masuk akan keluar lebih dahulu