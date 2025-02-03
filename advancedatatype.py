import heapq # untuk mengoperasikan heapify()

myList = [9, 5, 4, 1, 3, 2]
heapq.heapify(myList) # mengubah list menjadi heap
print(myList) # outputnya [1, 3, 2, 5, 9, 4]
print(myList[0]) # output nya pasti adalah 1 karena itu yang paling kecil

# heapify() digunakan untuk mengubah list biasa menjadi heap (struktur data binary heap)

heapq.heappush(myList, 10) # menambahkan angka 10 kedalam heap
print(myList)
x = heapq.heappop(myList) # menghapus dan mengembalikan elemen terkecil dari sebuah heap 
print(x) # outputnya 1 



