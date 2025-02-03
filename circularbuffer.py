from collections import deque

circular = deque(maxlen=5)

for i in range(7):
    circular.append(i)
    print("Deque:", circular)

#output:
#Deque: deque([0], maxlen=5)
#Deque: deque([0, 1], maxlen=5)
#Deque: deque([0, 1, 2], maxlen=5)
#Deque: deque([0, 1, 2, 3], maxlen=5)
#Deque: deque([0, 1, 2, 3, 4], maxlen=5)
#Deque: deque([1, 2, 3, 4, 5], maxlen=5)
#Deque: deque([2, 3, 4, 5, 6], maxlen=5)