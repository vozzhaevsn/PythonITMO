line1 = [1, 2, 3]
line2 = ['a', 'b', 'c']
line3 = []
for l in line1:
    line3.append(line1[l-1])
    line3.append(line2[l-1])

print(line3)