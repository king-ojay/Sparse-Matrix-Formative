#!/usr/bin/env python3
class SparseMatrix:
    def __init__(self, num_rows, num_cols):
        """
        Initializes an empty sparse matrix with the dimensions that are needed.
        The matrix is stored as a dictionary where the keys are ("row" and "col") tuples
        and values are the corresponding nonzero integers.
        """
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = {}  # Only nonzero entries are stored

           
