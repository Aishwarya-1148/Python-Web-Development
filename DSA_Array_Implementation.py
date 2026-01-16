# Creating an empty list (acts as array)

# ======== Array Real Life Use =============

"""
1️⃣ Array (Python List)
Where it is used:
    Storing data in ordered form
    Handling collections of similar data

Real Project Examples:
    Product list in e-commerce website
    Student marks or employee salary records
    Image pixels stored in row-column format
    Storing API response data

Why array is used:
    Fast access using index
    Easy traversal
    Efficient for read-heavy operations

"""

arr = []

# INSERT ELEMENTS INTO ARRAY
arr.append(50)
arr.append(20)
arr.append(30)
arr.append(10)
arr.append(5)
# -----------------------------------------
# DISPLAY ARRAY ELEMENTS
# -----------------------------------------
print("Array elements:")
for i in arr:
    print(i, end=" ")

# -----------------------------------------
# ACCESS ELEMENT BY INDEX
# -----------------------------------------
print("\nElement at index 2:", arr[2])

# -----------------------------------------
# UPDATE ELEMENT
# -----------------------------------------
arr[1] = 25
print("After update:", arr)

# -----------------------------------------
# DELETE ELEMENT
# -----------------------------------------
arr.remove(30)
print("After deletion:", arr)

# -----------------------------------------
# SEARCH ELEMENT
# -----------------------------------------
search = 40
if search in arr:
    print(search, "found in array")
else:
    print(search, "not found in array")

# =========================================
# BUBBLE SORT ALGORITHM : 
""" Quetion : Where do we need to sort the data in real application 
Answer : Better User Experience (UI / Display)
Real Project Examples
    Products sorted by price (low to high)
    Emails sorted by date
    Marks sorted in ascending/descending order
    Leaderboards in games
📌 Users expect sorted data.
"""
# =========================================
#                                          0   1   2   3 
# Bubble Sort Logic = Before Bubble Sort: [5, 10, 25, 50]
print("\nBefore Bubble Sort:", arr)

n = len(arr)
for i in range(0, n): # 2
    for j in range(i + 1, n): # 3
        if arr[i] > arr[j]: # 50 > 25
            # Swap if element at i is greater
            arr[i], arr[j] = arr[j], arr[i]

print("After Bubble Sort:", arr)



