# Defining
li1 = []
print("li1 outputnya:", li1) 
    # Output: li1 []

li2 = [4, 5, 6]
print("li2 outputnya:", li2)
# Output: li2 [4, 5, 6]

li3 = list((1, 2, 3))
print("li3 outputnya:", li3)
# Output: li3 [1, 2, 3]

li4 = list(range(1, 11))
print("li6 outputnya:", li4)
# Output: li6 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generate 
li5 = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print("li5 outputnya:", li5) # Output: li5 [1, 3, 5, 7, 9,..., 19]

li6 = [x ** 2 for x in range (1, 11) if x % 2 == 1]
print("li6 outputnya:", li6) # Output: li6 [1, 9, 25, 49, 81]

li7 = [x for x in [3, 4, 5, 6, 7] if x > 5]
print("li7 outputnya:", li7) # Output: li7 [6, 7]

li8 = list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))
print("li8 outputnya:", li8) # Output: li8 [6, 7]

# Append
li9 = []
li9.append(1) # Append 1 ke li9
print("li9 outputnya:", li9) 
# Output: li9 [1]
li9.append(2) # Append 2 ke li9
print("li9 outputnya:", li9)
# Output: li9 [1, 2]
li9.append(3) # Append 3 ke li9
print("li9 outputnya:", li9)
# Output: li9 [1, 2, 3]
li9.append(4) # Append 4 ke li9
print("li9 outputnya:", li9)
# Output: li9 [1, 2, 3, 4]

# List Slicing
# a_list[start:end]
# a_list[start:end:step]
    # Slicing
a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(a[2:6]) # Output: ['bacon', 'tomato', 'ham', 'lobster']
print(a[-5:-2]) # Output: ['egg', 'bacon', 'tomato']
print(a[1:4]) # Output: ['egg', 'bacon', 'tomato']

    # Omitting index
print(a[:4]) # Output: ['spam', 'egg', 'bacon', 'tomato']
print(a[0:4]) # Output: ['spam', 'egg', 'bacon', 'tomato']
print(a[2:]) # Output: ['bacon', 'tomato', 'ham', 'lobster']
print(a[2:len(a)]) # Output: ['bacon', 'tomato', 'ham', 'lobster']
print(a) # Output: ['spam', 'egg', 'bacon', 'tomato', 'ham',
print(a[:]) # Output: ['spam', 'egg', 'bacon', 'tomato', 'ham',

    # With a Stride
print(a[0:6:2]) # Output: ['spam', 'bacon', 'lobster']
print(a[1:6:2]) # Output: ['egg', 'tomato']
print(a[6:0:-2]) # Output: ['lobster', 'ham']
print(a) # Output: ['spam', 'egg', 'bacon', 'tomato', 'ham',
print(a[::-1]) # Output: ['lobster', 'ham', 'tomato', 'bacon',

# Remove
li10 = ['bread', 'butter', 'milk'] # List
print(li10.pop()) # Output: milk
print(li10) # Output: ['bread', 'butter']
del li10[0] # Delete bread
print(li10) # Output: ['butter']

# Access
li11 = ['a', 'b', 'c', 'd']
print(li11[0]) # Output: a
print(li11[-1]) # Output: d
print(li11[2]) # Output: c

# Concatenating
ood = [1, 3, 5]
(ood.extend([9, 11, 13])) 
print(ood) # Output: [1, 3, 5, 9, 11, 13
ood = [1, 3, 5]
print(ood + [9, 11, 13])
# Output: [1, 3, 5, 9, 11, 13

# sort & reverse
li12 = [3, 1, 4, 1, 5, 9]
li12.sort() # Sort in ascending order
print(li12) # Output: [1, 1, 3, 4,]
li12.reverse() # Reverse the list
print(li12) # Output: [4, 3, 1, 1, 5, 9]

# Count
li13 = [1, 2, 2, 3, 3, 3]
print(li13.count(3)) # Output: 3

# Repeating
li14 = ["re"] * 3
print(li14) # Output: ['re', 're', 're']