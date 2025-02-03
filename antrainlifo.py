from collections import deque

stack = deque()

stack.append("A") # menambahkan elemen (push)
stack.append("B")
stack.append("C")

print("Stack sebelum pop:", stack)

stack.pop() # menghapus elemen terakhir (pop)
print("Stack setelah 1 pop:", stack)

# LIFO (Last in, First Out) adalah elemen terakhir yang masuk akan keluar lebih dulu