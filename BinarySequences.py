def binary_sequences(sequence_length: int) -> list:
    # Base cases
    if sequence_length == 1:
        return [0, 1]
    if sequence_length == 2:
        return [(0, 0), (0, 1), (1, 0), (1, 1)]
    # Recursive step
    subsequences = binary_sequences(sequence_length - 1)
    return [tuple(list(subsequence) + [i]) for subsequence in subsequences for i in range(2)]
