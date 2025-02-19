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

   @classmethod
    def from_file(MatrixClass, file_path):
        """
        Creates a SparseMatrix from a file.
        
        Expected file format:
          - First non-empty line: "rows=<number>"
          - Second non-empty line: "cols=<number>"
          - Subsequent lines: "(row, col, value)" for each nonzero entry.
        
        The function strips out any blank lines or extra whitespace.
        If any line has the wrong format, it raises a ValueError.
        
        Note: I used 'MatrixClass' instead of 'cls'
              but they  serve the same purpose: referring to the class-SparseMatrix itself.
        """
    try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
        except Exception as e:
            raise ValueError(f"Error reading file: {e}")

        # Remove empty lines and  whitespace
        lines = [line.strip() for line in lines if line.strip()]
        if len(lines) < 2:
            raise ValueError("Input file has wrong format")           
