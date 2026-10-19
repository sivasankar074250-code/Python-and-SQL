# pyhton_practice_day_6

# 1. Dictionary Lookup 

stock = {'LED': 20, 'RESISTOR': 50, 'SENSOR': 4}
requested = ['LED', 'SENSOR', 'SWITCH']
for item in requested:
    quantity = stock.get(item)
    if quantity is None:
        print(f"{item}: unavailable")
    else:
        print(f"{item}: {quantity} available")

# 2. Set Operations 

a = {101, 102, 103, 105}
b = {102, 104, 105, 106}
print("Both courses:", sorted(a & b))
print("Only Course A:", sorted(a - b))
print("Either course:", sorted(a | b))

# 3. Invert a Dictionary

marks = {'Arun': 85, 'Priya': 92, 'Kavin': 78}
inverted = {value: key for key, value in marks.items()}
print(inverted)

# 4. Group Names by First Letter

names = ['Anu', 'Arun', 'Bala', 'Banu', 'Cathy', 'Asha']
groups = {}
for name in names:
    groups.setdefault(name[0].upper(), []).append(name)
print(groups)

# 5. Merge Inventory Dictionaries

store_a = {'LED': 20, 'Cable': 10, 'Board': 3}
store_b = {'Cable': 5, 'Sensor': 7, 'LED': 8}
combined = store_a.copy()
for item, quantity in store_b.items():
    combined[item] = combined.get(item, 0) + quantity
print("Combined inventory:", combined)

# 6. Rank Products 

sales = {'Sensor': [4, 6, 5], 'Cable': [10, 2, 3], 'Board': [8, 7], 'LED': [5, 5, 5]}
totals = {product: sum(values) for product, values in sales.items()}
for product, total in sorted(totals.items(), key=lambda item: (-item[1], item[0])):
    print(f"{product}: {total}")

# 7. Build a Nested Dictionary 

records = [('D01', 'Lab-A', 'READY'), ('D02', 'Lab-B', 'BUSY'), ('D01', 'Lab-C', 'MAINTENANCE')]
devices = {}
for device_id, location, status in records:
    devices[device_id] = {'location': location, 'status': status}
print(devices)

# 8. Find Common Permissions

permissions = {'admin': {'read', 'write', 'delete'}, 'operator': {'read', 'write'}, 'auditor': {'read', 'export'}}
sets = list(permissions.values())
print("Common permissions:", sorted(set.intersection(*sets)))
print("All permissions:", sorted(set.union(*sets)))

# 9. Subarray Sum Equals K

nums = [1, 1, 1]
k = 2
prefix_count = {0: 1}
prefix_sum = 0
count = 0
for num in nums:
    prefix_sum += num
    count += prefix_count.get(prefix_sum - k, 0)
    prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
print("Count:", count)

# 10. Minimum Window Substring

s = 'ADOBECODEBANC'
t = 'ABC'
need = {}
for char in t:
    need[char] = need.get(char, 0) + 1
left = 0
missing = len(t)
best_start = 0
best_length = float('inf')
window = {}
for right, char in enumerate(s):
    window[char] = window.get(char, 0) + 1
    if char in need and window[char] <= need[char]:
        missing -= 1
    while missing == 0:
        if right - left + 1 < best_length:
            best_start = left
            best_length = right - left + 1
        left_char = s[left]
        window[left_char] -= 1
        if left_char in need and window[left_char] < need[left_char]:
            missing += 1
        left += 1
result = "" if best_length == float('inf') else s[best_start:best_start + best_length]
print("Minimum window:", repr(result))

