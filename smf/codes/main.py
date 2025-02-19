from sparse_matrix import SparseMatrix

def main():
    print("DEBUG: main() started")
    print("Sparse Matrix Operations")
    print("Select an operation: add, subtract, multiply")
    op = input("Enter operation: ").strip().lower()
    """
    Main function to interact with the user:
      1. Prompts the user to choose an operation (add, subtract, multiply).
      2. Reads the file paths for two sparse matrices.
      3. Loads the matrices from the input files.
      4. Performs the selected operation.
      5. Outputs the resulting sparse matrix.
    """
    print("Sparse Matrix Operations")
    print("Select an operation: add, subtract, multiply")
    op = input("Enter operation: ").strip().lower()

    file1 = input("Enter path for the first matrix file: ").strip()
    file2 = input("Enter path for the second matrix file: ").strip()

    try:
        # Load the matrices from the specified files
        matrix1 = SparseMatrix.from_file(file1)
        matrix2 = SparseMatrix.from_file(file2)

        # Perform the selected operation
        if op == "add":
            result = matrix1 + matrix2
        elif op == "subtract":
            result = matrix1 - matrix2
        elif op == "multiply":
            result = matrix1 * matrix2
        else:
            print("Invalid operation selected.")
            return

        print("\nResultant Matrix:")
        print(result)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
