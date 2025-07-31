from typing import List
from src.models.product import Product


class Category:
    category_count = 0  # Количество категорий
    product_count = 0  # Количество товаров

    def __init__(self, name: str, description: str, products: List[Product]):
        """
        Инициализация экземпляра Category.

        Аргументы:
            name: Название категории
            description: Описание категории
            products: Список объектов Product в этой категории
        """
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)
