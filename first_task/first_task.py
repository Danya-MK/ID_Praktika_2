import numpy as np
import json


def process_matrix(input_file, output_file, json_file):
    matrix = np.load(input_file)

    total_sum = int(np.sum(matrix))
    total_mean = round(float(np.mean(matrix)), 0)

    main_diag = np.diagonal(matrix)
    sum_main_diag = int(np.sum(main_diag))
    mean_main_diag = round(float(np.mean(main_diag)), 0)

    secondary_diag = np.diagonal(np.fliplr(matrix))
    sum_secondary_diag = int(np.sum(secondary_diag))
    mean_secondary_diag = round(float(np.mean(secondary_diag)), 0)

    max_value = int(np.max(matrix))
    min_value = int(np.min(matrix))

    results = {
        "sum": total_sum,
        "avr": total_mean,
        "sumMD": sum_main_diag,
        "avrMD": mean_main_diag,
        "sumSD": sum_secondary_diag,
        "avrSD": mean_secondary_diag,
        "max": max_value,
        "min": min_value,
    }

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    normalized_matrix = (matrix - min_value) / (max_value - min_value)

    np.save(output_file, normalized_matrix)

    print(f"Результаты сохранены в файл {json_file}")
    print(f"Нормализованная матрица сохранена в файл {output_file}")


if __name__ == "__main__":
    input_file = "C:/ProjectsPython/ID_Praktika_2/first_task.npy"
    output_file = "normalized.npy"
    json_file = "results.json"
    process_matrix(input_file, output_file, json_file)
