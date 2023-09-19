"""Здесь надо написать тесты с использованием pytest для модуля item."""

# Импорт класса Item из вашего модуля
from src.item import Item, InstantiateCSVError
from src.phone import Phone
import os
import csv
import pytest


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


# тесты homework 6
def test_instantiate_from_csv_existing_file():
    # Создаем временный CSV файл с данными
    with open('test_items.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'price', 'quantity'])
        writer.writerow(['Item 1', '10.0', '5'])
    # Проверяем, что метод работает без ошибок
    Item.instantiate_from_csv(os.path.abspath('test_items.csv'))
    # Очищаем временный файл
    os.remove('test_items.csv')


def test_instantiate_from_csv_nonexistent_file():
    # Проверяем, что метод выбрасывает FileNotFoundError
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('nonexistent.csv')


# Тестовые случаи для InstantiateCSVError
def test_instantiate_csv_error_message():
    # Проверяем сообщение об ошибке в InstantiateCSVError
    error = InstantiateCSVError("Файл item.csv поврежден")
    assert str(error) == "Файл item.csv поврежден"

def test_instantiate_from_csv_corrupted_file():
    # Создаем временный CSV файл с поврежденными данными
    with open('corrupted_items.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'price'])
        writer.writerow(['Item 1', '10.0'])
    try:
        Item.instantiate_from_csv(os.path.abspath('corrupted_items.csv'))
    except InstantiateCSVError:
        # Проверяем, что метод выбросил исключение InstantiateCSVError
        pass
    else:
        # Если исключение не было выброшено, то тест не прошел
        assert False, "Ожидалось, что метод выбросит InstantiateCSVError"
    os.remove('corrupted_items.csv')


