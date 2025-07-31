from src.models.product import Product
from src.models.category import Category
from src.utils.file_loader import load_data_from_json


def main():
    # Пример использования из задания
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(Category.category_count)
    print(Category.product_count)

    # Загрузка из JSON
    try:
        categories = load_data_from_json("data/products.json")
        print(f"Загружено {len(categories)} категорий")
        for category in categories:
            print(f"Категория: {category.name}, Товаров: {len(category.products)}")
    except FileNotFoundError as e:
        print(f"Ошибка загрузки данных: {e}")


if __name__ == "__main__":
    main()
