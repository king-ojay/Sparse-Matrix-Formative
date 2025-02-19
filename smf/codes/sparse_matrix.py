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

# Parse the number of rows
        if not lines[0].startswith("rows="):
            raise ValueError("Input file has wrong format")
        try:
            num_rows = int(lines[0].split('=')[1])
        except Exception:
            raise ValueError("Input file has wrong format")

        # Parse the number of columns
        if not lines[1].startswith("cols="):
            raise ValueError("Input file has wrong format")
        try:
            num_cols = int(lines[1].split('=')[1])
        except Exception:
            raise ValueError("Input file has wrong format")

        # Create a new matrix using MatriClass
        matrix = MatrixClass(num_rows, num_cols)

        # Process subsequent lines containing nonzero entries
        for idx, line in enumerate(lines[2:], start=3):
            if not (line.startswith("(") and line.endswith(")")):
                raise ValueError("Input file has wrong format")
            inner = line[1:-1]
            parts = inner.split(',')
            if len(parts) != 3:
                raise ValueError("Input file has wrong format")
            try:
                row = int(parts[0].strip())
                col = int(parts[1].strip())
                value = int(parts[2].strip())
            except Exception:
                raise ValueError("Input file has wrong format")
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                raise ValueError("Input file has wrong format")
            if value != 0:
                matrix.data[(row, col)] = value

        return matrix

