"""Здесь надо написать тесты с использованием pytest для модуля item."""

# Импорт класса Item из вашего модуля
from src.item import Item
from src.phone import Phone


# Тест на расчет общей стоимости товара
def test_calculate_total_price():
    item = Item("Товар 1", 100, 5)
    total_price = item.calculate_total_price()
    assert total_price == 500  # Проверяем, что общая стоимость рассчитана правильно

# Тест на применение скидки
def test_apply_discount():
    item = Item("Товар 2", 200, 3)
    item.apply_discount()
    assert item.price == 200  # Проверяем, что цена уменьшилась на 20% после скидки

# Тест на добавление товара в атрибут all
def test_add_item_to_all():
    item = Item("Товар 3", 50, 10)
    assert item in Item.all  # Проверяем, что созданный товар добавлен в список всех товаров

# Тест для применения скидки
def test_apply_discount_rate():
    item = Item("Товар 4", 200, 3)
    item.pay_rate = 0.9  # Устанавливаем скидку 10%
    item.apply_discount()
    assert item.price == 180

# Тестирование метода string_to_number
def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr():
    item = Item("Смартфон", 10000, 20)
    expected_repr = "Item(Смартфон, 10000, 20)"
    assert repr(item) == expected_repr

def test_str():
    item = Item("Смартфон", 10000, 20)
    expected_str = "Смартфон"
    assert str(item) == expected_str

def test_item_addition():
    item1 = Item("Item 1", 10, 5)
    item2 = Item("Item 2", 20, 3)
    phone = Phone("Phone", 200, 2, 1)

    assert item1 + item2 == 8
    assert item1 + phone == 7
