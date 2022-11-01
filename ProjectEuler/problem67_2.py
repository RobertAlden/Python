file = open("p067_triangle.txt","r")
triangle = []
while True:
    row = file.readline().split()
    if not row:
        break
    row = [int(i) for i in row]
    triangle.append(row)

length = 100

for r in range(length-2,-1,-1):
    for i in range(r+1):
        triangle[r][i] += max(triangle[r+1][i],triangle[r+1][i+1])

print(triangle[0][0])