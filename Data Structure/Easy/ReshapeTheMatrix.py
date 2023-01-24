def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    # generating a list with all the elements from the matrix
    list_el = [el for els in mat for el in els]
    # checking if the matrix can be reshapped into a new one
    if len(mat)*len(mat[0]) == r*c:
        return [list_el[i:i+c] for i in range(0, len(list_el), c)]
    return mat
