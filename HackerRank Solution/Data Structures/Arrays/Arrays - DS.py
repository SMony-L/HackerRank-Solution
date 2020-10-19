arr = [1,4,3,2]

# Slicing
print(arr[::-1])

# Using reversed()
print([i for i in reversed(arr)])

# Brute Force
index = len(arr)
newList = [0]* index
for i in arr:
    index = index - 1
    newList[index] = i
print(newList)
