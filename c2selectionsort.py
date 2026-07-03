marks = [55, 91, 68, 80, 74]

for i in range(len(marks)):
    big = i
    for j in range(i+1, len(marks)):
        if marks[j] > marks[big]:
            big = j
    marks[i], marks[big] = marks[big], marks[i]

print("Top 3 :", marks[0:3])