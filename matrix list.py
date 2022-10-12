matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

my_list = []

for i in range(len(matrix[0])):
    your_list = []
    for j in matrix:
        your_list.append(j[i])
        
    my_list.append(your_list)

print(my_list)
