# Levenshtein Distance
# Gaurav Arya
def levenshtein_matrix(s1, s2):
    n = len(s1)
    m = len(s2)
    mat = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        mat[i][0] = i
    for j in range(m + 1):
        mat[0][j] = j



    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                mat[i][j] = mat[i - 1][j - 1]
            else:
                mat[i][j] = 1 + min(
                    mat[i - 1][j],   # remove
                    mat[i][j - 1],   # add
                    mat[i - 1][j - 1] # change
                )
    return mat

# Printing the matrix
def print_matrix(matrix, s1, s2):
    print("     ", end="")
    for ch in s2:
        print(f"{ch:>4}", end="")
    print()
    
    for i in range(len(matrix)):
        if i == 0:
            print(" ", end="")
        else:
            print(s1[i - 1], end="")
        for val in matrix[i]:
            print(f"{val:4}", end="")
        print()

pairs = [
    ("Levenshtein", "Lavenstaein"),
    ("TryHackMe", "TriHackingMe"),
    ("Optimization", "Progressive"),
    ("This is easy", "This is easy")
]
for first, second in pairs:
    print("\n")
    print(f"Matrix for: '{first}'  '{second}'")
    
    final_matrix = levenshtein_matrix(first, second)
    print_matrix(final_matrix, first, second)
    
    print(f"\nEdit Distance is = {final_matrix[len(first)][len(second)]}")
