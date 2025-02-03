import heapq

tugas = [(3, "kerjakan PR"), (1, "Makan"), (2, "Tidur"), (4, "Mandi")]


heapq.heapify(tugas)  # ubah menjadi heap

while tugas: # susun tugas berdasarkan prioritas
    prioritas, kegiatan = heapq.heappop(tugas)
    print(f"{kegiatan} (prioritas {prioritas})")

