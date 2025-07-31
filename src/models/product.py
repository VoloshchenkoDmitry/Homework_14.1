class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация экземпляра Product.

        Аргументы:
            name: Название товара
            description: Описание товара
            price: Цена товара (может включать копейки)
            quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
