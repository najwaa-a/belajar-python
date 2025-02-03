import heapq

data = [7, 1, 4, 8, 2]
heapq.heapify(data)

sorted_data = [heapq.heappop(data) for _ in range(len(data))]
print(sorted_data) # outputnya: [1, 2, 4, 7, 8] terurut naik
