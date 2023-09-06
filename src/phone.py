from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        '''
        Инициализируем дочерний класс.
        Добавляем дополнительно атрибут, содержащий
        количество поддерживаемых сим-карт
        '''
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        '''
        Добавляем магический метод repr
        '''
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        '''
        Добавляем магический метод сложения add
        Реализуем проверку сложения `Phone` или `Item`
        с экземплярами не `Phone` или `Item` классов.
        '''
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Нельзя сложить Phone с объектом другого типа")
