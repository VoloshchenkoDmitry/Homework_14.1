import pytest
from src.models.product import Product


@pytest.fixture
def sample_product():
    return Product("Тестовый товар", "Тестовое описание", 100.50, 10)


def test_product_initialization(sample_product):
    assert sample_product.name == "Тестовый товар"
    assert sample_product.description == "Тестовое описание"
    assert sample_product.price == 100.50
    assert sample_product.quantity == 10


def test_product_attributes_types(sample_product):
    assert isinstance(sample_product.name, str)
    assert isinstance(sample_product.description, str)
    assert isinstance(sample_product.price, float)
    assert isinstance(sample_product.quantity, int)
