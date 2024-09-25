a = [1, 8, 6, 2, 5, 4, 8, 3, 7]

maxArea = 0

start = 0
end = len(a) - 1

while start <= end:
    area = (end - start) * min(a[end], a[start])

    if area > maxArea:
        maxArea = area
    
    if a[end] < a[start]:
        end -= 1
        continue

    start += 1

print(maxArea)
