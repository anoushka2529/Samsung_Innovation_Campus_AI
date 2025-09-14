import numpy as np

# Define the matrix A
A = np.array([[2, 3],
              [3, -6]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix A:\n", A)
print("\nEigenvalues:", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)

# Characteristic polynomial (det(A - λI))
# For demonstration, let's compute manually using np.poly
char_poly = np.poly(A)  # coefficients of λ^2 + 4λ - 21
print("\nCharacteristic Polynomial coefficients:", char_poly)
