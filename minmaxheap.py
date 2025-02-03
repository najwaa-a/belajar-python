import heapq

myList = [9, 5, 4, 1, 3, 2] # list awal
myList = [-val for val in myList] # mengubah list menjadi negatif
heapq.heapify(myList) # mengubah list menjadi heap

x = heapq.heappop(myList) # mengambil elemen paling kecil 
print(-x) # mengembalikan nilai positif 