import numpy as np
import trimesh

def load_stl(file_path):
    return trimesh.load_mesh(file_path)

def save_stl(mesh, file_path):
    mesh.export(file_path)

def apply_transformation(mesh, transformation_matrix):
    # Apply the transformation matrix to all vertices
    mesh.vertices = np.dot(mesh.vertices, transformation_matrix.T)
    return mesh

def skew_compensation(file_path, output_path, skew_matrix):
    # Load the STL file
    mesh = load_stl(file_path)
    
    # Compute the inverse of the skew matrix for compensation
    inverse_skew_matrix = np.linalg.inv(skew_matrix)
    
    # Apply the inverse skew transformation
    compensated_mesh = apply_transformation(mesh, inverse_skew_matrix)
    
    # Save the compensated mesh to a new STL file
    save_stl(compensated_mesh, output_path)
    
    print(f"Skew compensation completed. Saved to {output_path}")

# Example usage
input_stl_file = 'Name.stl'
output_stl_file = 'compensated_Name.stl'

# Define the skew matrixS
skew_matrix = np.array([
    [1, -0.0012, 0],  # Skew in X direction
    [0, 1, 0],  # Skew in Y direction
    [0, 0, 1]
])

# Perform skew compensation
skew_compensation(input_stl_file, output_stl_file, skew_matrix)
