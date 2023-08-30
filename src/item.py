import os
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        '''
        Создание приватного аттрибута name
        '''
        return self._name

    @name.setter
    def name(self, value):
        '''
        Обрезает длину наименования до 10 символов
        '''
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        '''
        Класс-метод, инициализирующий экземпляры
        класса `Item` данными из файла _src/items.csv_
        '''
        filename = os.path.split(filename)
        CSV_PATH = os.path.join(os.path.dirname(os.getcwd()), *filename)
        with open(CSV_PATH) as file:
            csv_reader = csv.DictReader(file)
            cls.all.clear()
            for row in csv_reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string):
        '''
        Cтатический метод, возвращающий число из числа-строки
        '''
        return int(float(string))
