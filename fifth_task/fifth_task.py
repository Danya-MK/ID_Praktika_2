import pandas as pd
import msgpack
import json
import os

file_path = "Assignment.csv"

data = pd.read_csv(file_path, sep=",", encoding="utf-8", low_memory=False)

selected_columns = [
    "BillNo",
    "Itemname",
    "Quantity",
    "Date",
    "Price",
    "CustomerID",
    "Country",
]
selected_data = data[selected_columns]

selected_data["Quantity"] = pd.to_numeric(selected_data["Quantity"], errors="coerce")
selected_data["Price"] = selected_data["Price"].str.replace(",", ".").astype(float)

numerical_columns = ["Quantity", "Price", "CustomerID"]
statistics = {}

for column in numerical_columns:
    col_data = selected_data[column]
    statistics[column] = {
        "max": col_data.max(),
        "min": col_data.min(),
        "mean": col_data.mean(),
        "sum": col_data.sum(),
        "std": col_data.std(),
    }

text_column = "Country"
text_frequency = selected_data[text_column].value_counts().to_dict()

statistics = {
    k: {key: float(value) for key, value in v.items()} for k, v in statistics.items()
}
analysis_results = {
    "numerical_analysis": statistics,
    "text_frequency": text_frequency,
}

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(analysis_results, f, ensure_ascii=False, indent=4)

selected_data.to_csv("data.csv", index=False, sep=";")
selected_data.to_json("data.json", orient="records", indent=4)
selected_data.to_pickle("data.pkl")
with open("data.msgpack", "wb") as f:
    packed = msgpack.packb(selected_data.to_dict(orient="records"))
    f.write(packed)

file_formats = [
    "data.csv",
    "data.json",
    "data.pkl",
    "data.msgpack",
]
file_sizes = {file: os.path.getsize(file) for file in file_formats}

with open("file_size.txt", "w", encoding="utf-8") as f:
    f.write("Размеры файлов в байтах:\n")
    for file, size in file_sizes.items():
        f.write(f"{file}: {size} байт\n")
