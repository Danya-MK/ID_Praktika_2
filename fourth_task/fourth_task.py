import pickle
import json
import os


def update_prices(products_file, price_updates_file, output_file):
    with open(products_file, "rb") as file:
        products = pickle.load(file)

    with open(price_updates_file, "r", encoding="utf-8") as file:
        price_updates = json.load(file)

    for update in price_updates:
        name = update.get("name")
        method = update.get("method")
        param = update.get("param")

        for product in products:
            if product.get("name") == name:
                current_price = product.get("price", 0)

                if method == "add":
                    product["price"] = current_price + param
                elif method == "sub":
                    product["price"] = max(0, current_price - param)
                elif method == "percent+":
                    product["price"] = current_price * (1 + param)
                elif method == "percent-":
                    product["price"] = current_price * (1 - param)

                product["price"] = max(0, product["price"])

    with open(output_file, "wb") as file:
        pickle.dump(products, file)

    print(f"Модифицированные данные сохранены в {output_file}")


if __name__ == "__main__":
    products_file = "fourth_task_products.json"
    price_updates_file = "fourth_task_updates.json"

    output_file = "results.pkl"

    update_prices(products_file, price_updates_file, output_file)
