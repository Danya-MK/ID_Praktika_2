import numpy as np
import os


def process_matrix_and_save(input_file, output_file_npz, output_file_compressed):
    matrix = np.load(input_file)

    indices = np.where(matrix > 514)
    x, y = indices[0], indices[1]
    z = matrix[indices]

    np.savez(output_file_npz, x=x, y=y, z=z)
    np.savez_compressed(output_file_compressed, x=x, y=y, z=z)

    size_npz = os.path.getsize(output_file_npz)
    size_compressed = os.path.getsize(output_file_compressed)

    print(f"Размер файла {output_file_npz}: {size_npz} байт")
    print(f"Размер файла {output_file_compressed}: {size_compressed} байт")


if __name__ == "__main__":
    input_file = "second_task.npy"

    output_file_npz = "result.npz"
    output_file_compressed = "result_compressed.npz"

    process_matrix_and_save(input_file, output_file_npz, output_file_compressed)
