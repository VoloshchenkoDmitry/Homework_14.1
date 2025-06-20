import json
from typing import List, Dict, Any
from pathlib import Path
from src.models.product import Product
from src.models.category import Category


def load_data_from_json(file_path: str) -> List[Category]:
    """
    Загрузка данных о категориях и товарах из JSON-файла.

    Аргументы:
        file_path: Путь к JSON-файлу

    Возвращает:
        Список объектов Category, заполненных объектами Product
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = []
    for category_data in data:
        products = [
            Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
            )
            for product_data in category_data['products']
        ]
        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            products=products
        )
        categories.append(category)

    return categories
