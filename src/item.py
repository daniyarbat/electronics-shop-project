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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        '''
        Создание машического метода repr
        '''
        return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.quantity})"

    def __str__(self):
        '''
        Создание метода str
        '''
        return f'{self.__name}'

    @property
    def name(self):
        '''
        Создание приватного аттрибута name
        '''
        return self.__name

    @name.setter
    def name(self, value):
        '''
        Обрезает длину наименования до 10 символов
        '''
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

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

    def __add__(self, other):
        '''
           Добавляем магический метод сложения add
           Реализуем проверку сложения `Phone` или `Item`
           с экземплярами не `Phone` или `Item` классов.
        '''
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Нельзя сложить Item с объектом другого типа")
