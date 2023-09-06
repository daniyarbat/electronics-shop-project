from src.phone import Phone
from src.item import Item

def test_phone_creation():
    phone = Phone("Phone Model", 500, 10, 2)
    assert phone.name == "Phone Model"
    assert phone.price == 500
    assert phone.quantity == 10
    assert phone.number_of_sim == 2

def test_phone_addition():
    phone1 = Phone("Phone 1", 100, 5, 1)
    phone2 = Phone("Phone 2", 200, 3, 2)
    item = Item("Item", 50, 10)

    assert phone1 + phone2 == 8  # Сумма количества Phone 1 и Phone 2
    assert phone1 + item == 15  # Сумма количества Phone 1 и Item
    assert item + phone2 == 13  # Сумма количества Item и Phone 2