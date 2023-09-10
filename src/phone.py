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

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if isinstance(number_of_sim, int) and number_of_sim > 0:
            self._number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        '''
        Добавляем магический метод repr
        '''
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
