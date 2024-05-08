def normalized_vector(vector: tuple) -> tuple:
    norm = sum(map(lambda x: x ** 2, vector)) ** (1/2)
    return tuple([vi / norm for vi in vector])
