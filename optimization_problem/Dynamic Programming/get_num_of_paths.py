# ================== Recursion =======================
# def paths(matrix, i=0, j=0):
#     n, m = len(matrix), len(matrix[0])
#     if i >=  n or j >= m or matrix[i][j] == 1:
#         return 0
#     elif i == n-1 and j == m-1:
#         return 1
#     else:
#         return paths(matrix, i, j+1) + paths(matrix, i+1, j)


matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


class counter():

    def get_paths(self, matrix, i, j):
        n, m = len(matrix), len(matrix[0])
        if i >= n or j >= m or matrix[i][j] == 1:
            return 0
        elif i == n - 1 and j == m - 1:
            # self.paths += 1
            return 1
        else:
            return self.get_paths(matrix, i, j + 1) + self.get_paths(matrix, i + 1, j)

# =========== ANOTHER WAY ==============
    def __init__(self):
        self.paths = 0

    def get_paths(self, matrix, i, j):
        n, m = len(matrix), len(matrix[0])
        if i >= n or j >= m or matrix[i][j] == 1:
            return 0
        elif i == n - 1 and j == m - 1:
            self.paths += 1
        else:
            self.get_paths(matrix, i, j + 1)
            self.get_paths(matrix, i + 1, j)

        return self.paths

##=========================== Tabaulation ============================#


def get_paths(matrix):
    n, m = len(matrix), len(matrix[0])
    dp = [([0]*m) for i in range(n)]
    dp[0][0] = 1 if (matrix[0][0] == 0) else 0
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] if matrix[0][j] == 0 else 0
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] if matrix[i][0] == 0 else 0
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] if matrix[i][j] == 0 else 0
    return dp[n-1][m-1]
# =========== optimised in space complexity ===================#


def get_paths(matrix):
    n, m = len(matrix), len(matrix[0])
    prev_dp = [0]*m
    dp = [0]*m
    prev_dp[0] = 1 if (matrix[0][0] == 0) else 0
    for j in range(1, m):
        prev_dp[j] = prev_dp[j-1] if matrix[0][j] == 0 else 0
    for i in range(1, n):
        dp[0] = prev_dp[0] if matrix[i][0] == 0 else 0
        for j in range(1, m):
            dp[j] = prev_dp[j] + dp[j-1] if matrix[i][j] == 0 else 0
        prev_dp = dp
        dp = [0]*m
    return prev_dp[m-1]


obj = counter()
print(obj.get_paths(matrix, i=0, j=0))
# ===============
