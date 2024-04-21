def mat_to_list(adj_mat):
    adj_list = []
    for i in range(len(adj_mat)):
        neighbors = []
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] != 0:
                neighbors.append(j)
        adj_list.append(neighbors)
    return adj_list    
        
adj_mat = [
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]


adj_list = mat_to_list(adj_mat)
for i, neighbors in enumerate(adj_list):
    print(f"{neighbors}")
