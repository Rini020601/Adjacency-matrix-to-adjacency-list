import unittest

def mat_to_list(adj_mat):
    adj_list = []
    for i in range(len(adj_mat)):
        neighbors = []
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] != 0:
                neighbors.append(j)
        adj_list.append(neighbors)
    return adj_list

class TestMatToList(unittest.TestCase):

    def test_mat_to_list(self):
        adj_mat = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        expected_adj_list = [
            [1, 3],
            [2],
            [0],
            [4],
            [3],
            []
        ]
        adj_list = mat_to_list(adj_mat)
        self.assertEqual(adj_list, expected_adj_list)

if __name__ == '__main__':
    unittest.main()
