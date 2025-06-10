a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
count_0 = a.count(0)
count_1 = a.count(1)
count_2 = a.count(2)

sorted_a = [0]*count_0 + [1]*count_1 + [2]*count_2
print(sorted_a)