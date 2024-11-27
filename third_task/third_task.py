import json
import msgpack
import os
from collections import defaultdict


def process_products(input_file, json_output, msgpack_output):
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    aggregated_data = defaultdict(lambda: {"prices": []})

    for product in data:
        name = product.get("name", "Unknown")
        price = product.get("price")
        if isinstance(price, (int, float)):
            aggregated_data[name]["prices"].append(price)

    result = {}
    for name, values in aggregated_data.items():
        prices = values["prices"]
        if prices:
            result[name] = {
                "avg_price": round(sum(prices) / len(prices), 2),
                "max_price": max(prices),
                "min_price": min(prices),
            }

    with open(json_output, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)

    with open(msgpack_output, "wb") as file:
        msgpack.pack(result, file)

    json_size = os.path.getsize(json_output)
    msgpack_size = os.path.getsize(msgpack_output)
    print(f"Размер JSON файла: {json_size} байт")
    print(f"Размер MessagePack файла: {msgpack_size} байт")


if __name__ == "__main__":
    input_file = "third_task.json"

    json_output = "results.json"
    msgpack_output = "results.msgpack"

    process_products(input_file, json_output, msgpack_output)
