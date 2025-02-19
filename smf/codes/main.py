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
              but they serve the same purpose: referring to the class (SparseMatrix) itself.
        """
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
        except Exception as e:
            raise ValueError("Error reading file: {}".format(e))

        # Remove empty lines and whitespace
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

        # Create a new matrix using MatrixClass
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

    def getElement(self, row, col):
        """
        Returns the element at the given (row, col) position.
        If the element is not explicitly stored, returns 0.
        """
        if row < 0 or row >= self.num_rows or col < 0 or col >= self.num_cols:
            raise IndexError("Index out of bounds")
        return self.data.get((row, col), 0)

    def setElement(self, row, col, value):
        """
        Sets the element at the given (row, col) to the specified value.
        If value is 0, removes the entry from the storage to keep the matrix sparse.
        """
        if row < 0 or row >= self.num_rows or col < 0 or col >= self.num_cols:
            raise IndexError("Index out of bounds")
        if value == 0:
            self.data.pop((row, col), None)
        else:
            self.data[(row, col)] = value

    def __add__(self, other):
        """
        Overloads the '+' operator to add two sparse matrices.
        Both matrices must have the same dimensions.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for addition")
        result = SparseMatrix(self.num_rows, self.num_cols)
        # Copy self data
        for key, value in self.data.items():
            result.data[key] = value
        # Add entries from the other matrix
        for key, value in other.data.items():
            result.data[key] = result.getElement(*key) + value
            if result.data[key] == 0:
                del result.data[key]
        return result

    def __sub__(self, other):
        """
        Overloads the '-' operator to subtract one sparse matrix from another.
        Both matrices must have the same dimensions.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        result = SparseMatrix(self.num_rows, self.num_cols)
        # Copy self data
        for key, value in self.data.items():
            result.data[key] = value
        # Subtract entries from the other matrix
        for key, value in other.data.items():
            result.data[key] = result.getElement(*key) - value
            if result.data[key] == 0:
                del result.data[key]
        return result

    def __mul__(self, other):
        """
        Overloads the '*' operator to multiply two sparse matrices.
        The number of columns in the first matrix must equal the number of rows in the second.
        """
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(self.num_rows, other.num_cols)
        # Build an index for the second matrix to speed up multiplication
        other_index = {}
        for (row, col), value in other.data.items():
            other_index.setdefault(row, []).append((col, value))
        # Multiply only nonzero entries
        for (i, k), a_val in self.data.items():
            if k in other_index:
                for j, b_val in other_index[k]:
                    new_val = result.getElement(i, j) + a_val * b_val
                    result.setElement(i, j, new_val)
        return result

    def __str__(self):
        """
        Returns a string representation of the sparse matrix in the format:
          rows=<num_rows>
          cols=<num_cols>
          (i, j, value)
        for each nonzero entry.
        """
        lines = ["rows={}".format(self.num_rows), "cols={}".format(self.num_cols)]
        for (i, j), val in sorted(self.data.items()):
            lines.append("({}, {}, {})".format(i, j, val))
        return "\n".join(lines)
