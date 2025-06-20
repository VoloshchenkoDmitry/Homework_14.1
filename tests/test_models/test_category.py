import pytest
from src.models.category import Category
from src.models.product import Product


@pytest.fixture
def sample_products():
    return [
        Product("Товар 1", "Описание 1", 100.0, 5),
        Product("Товар 2", "Описание 2", 200.0, 10)
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Тестовая категория", "Тестовое описание", sample_products)


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Тестовая категория"
    assert sample_category.description == "Тестовое описание"
    assert len(sample_category.products) == 2
    assert sample_category.products == sample_products


def test_category_class_attributes(sample_category):
    assert Category.category_count > 0
    assert Category.product_count >= len(sample_category.products)


def test_multiple_categories(sample_products):
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    category1 = Category("Категория 1", "Описание 1", sample_products)
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + len(sample_products)

    category2 = Category("Категория 2", "Описание 2", sample_products[:1])
    assert Category.category_count == initial_category_count + 2
    assert Category.product_count == initial_product_count + len(sample_products) + 1
