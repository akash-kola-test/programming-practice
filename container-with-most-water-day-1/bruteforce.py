a = [1, 8, 6, 2, 5, 4, 8, 3, 7]

max_area_container = 0

for i in range(0, len(a)):
    for j in range(i, len(a)):
        if max_area_container < (min(a[i], a[j]) * (j - i)):
            max_area_container = (min(a[i], a[j]) * (j - i))

print(max_area_container)
